# Skill: Auto Git Pull and PR Helper

This skill is a self-contained Python helper that automatically detects the current Git repository, fetches from `origin`, pulls the current branch, and then checks whether a pull request should be created.

The script does not prompt the user; it can also generate a clean PR title and body automatically and create a GitHub pull request if `GITHUB_TOKEN` is available.

```python
import json
import os
import re
import subprocess
import sys
import urllib.request
import urllib.error


def run_git_command(args, check=False):
    return subprocess.run(args, capture_output=True, text=True, check=check)


def find_git_root():
    path = os.path.abspath(os.getcwd())
    while True:
        if os.path.isdir(os.path.join(path, '.git')):
            return path
        parent = os.path.dirname(path)
        if parent == path:
            raise FileNotFoundError('No git repository found in current directory or parents.')
        path = parent


def parse_github_repo(remote_url):
    patterns = [
        r'github\.com[:/](?P<owner>[^/]+)/(?P<repo>[^/]+?)(?:\.git)?$',
    ]
    for pattern in patterns:
        match = re.search(pattern, remote_url)
        if match:
            return match.group('owner'), match.group('repo')
    return None, None


def github_api_request(url, token=None, method='GET', data=None):
    headers = {'Accept': 'application/vnd.github+json'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    body = None
    if data is not None:
        body = json.dumps(data).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    request = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        message = exc.read().decode('utf-8', errors='ignore')
        raise RuntimeError(f'GitHub API error {exc.code}: {message}')


def get_default_branch():
    result = run_git_command(['git', 'remote', 'show', 'origin'])
    for line in result.stdout.splitlines():
        if 'HEAD branch:' in line:
            return line.split(':', 1)[1].strip()
    return 'main'


def generate_pr_title(branch, last_commit):
    branch_label = re.sub(r'[-_/]+', ' ', branch).strip().title()
    commit_title = last_commit.strip()
    if commit_title:
        return f'{branch_label}: {commit_title}'
    return f'Update {branch_label}'


def generate_pr_body(branch, commit_lines):
    lines = ['Automatic pull request created by skill helper.', f'Branch: {branch}', '']
    if commit_lines:
        lines.append('Commits included:')
        lines.extend(f'- {line}' for line in commit_lines)
    else:
        lines.append('No new commits were found to summarize.')
    return '\n'.join(lines)


def sanitize_branch_name(name, prefix='AI-'):
    slug = re.sub(r'[^0-9A-Za-z]+', '-', name).strip('-')
    if not slug:
        slug = 'ai-pr'
    return f'{prefix}({slug})'


def find_existing_pr(owner, repo, branch, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls?state=open&head={owner}:{branch}'
    prs = github_api_request(url, token=token)
    return prs[0] if prs else None


def create_pull_request(owner, repo, base, head, title, body, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls'
    data = {'title': title, 'body': body, 'head': head, 'base': base}
    return github_api_request(url, token=token, method='POST', data=data)


def main():
    repo_root = find_git_root()
    os.chdir(repo_root)
    print(f'📂 Git repository root detected: {repo_root}')

    try:
        branch = run_git_command(['git', 'branch', '--show-current'], check=True).stdout.strip()
    except subprocess.CalledProcessError as err:
        print('❌ Не вдалося визначити поточну гілку:', err.stderr.strip())
        return 1

    if not branch:
        print('❌ Поточна гілка не визначена.')
        return 1

    print(f'🔀 Поточна гілка: {branch}')

    try:
        last_commit = run_git_command(['git', 'log', '-1', '--pretty=%s', branch], check=True).stdout.strip()
        title = generate_pr_title(branch, last_commit)
        target_branch = branch
        if not branch.startswith('AI-'):
            target_branch = sanitize_branch_name(title)
            print(f'🌿 Створюю або перемикаюся на PR-гілку: {target_branch}')
            existing_branches = [b.strip().replace('* ', '') for b in run_git_command(['git', 'branch']).stdout.splitlines()]
            if target_branch in existing_branches:
                run_git_command(['git', 'checkout', target_branch], check=True)
            else:
                run_git_command(['git', 'checkout', '-b', target_branch], check=True)
            branch = target_branch

        remotes = run_git_command(['git', 'remote'], check=True).stdout.splitlines()
        if 'origin' not in remotes:
            print('❌ Віддалений репозиторій origin не знайдено.')
            return 1

        origin_url = run_git_command(['git', 'config', '--get', 'remote.origin.url'], check=True).stdout.strip()
        owner, repo = parse_github_repo(origin_url)
        default_branch = get_default_branch()

        print('🌐 Отримую оновлення з origin...')
        run_git_command(['git', 'fetch', 'origin'], check=True)

        remote_branch_exists = bool(run_git_command(['git', 'ls-remote', '--heads', 'origin', branch]).stdout.strip())
        if remote_branch_exists:
            print('⬇️ Пулю поточну гілку...')
            run_git_command(['git', 'pull', '--ff-only', 'origin', branch], check=True)
        else:
            print(f'⚠️ Remote branch origin/{branch} не знайдено. Далі буде створено PR без попереднього pull.')
            print(f'📤 Пушу нову гілку {branch} до origin...')
            run_git_command(['git', 'push', '-u', 'origin', branch], check=True)

        ahead_behind = run_git_command(['git', 'rev-list', '--left-right', '--count', f'origin/{default_branch}...{branch}'], check=True).stdout.strip()
        behind, ahead = map(int, ahead_behind.split())

        if ahead <= 0:
            print(f'ℹ️ Гілка {branch} не відрізняється від {default_branch}.')
            return 0

        print(f'✨ Branch is ahead of {default_branch} by {ahead} commit(s). Preparing PR info...')
        commits = run_git_command(['git', 'log', '--oneline', f'origin/{default_branch}..{branch}'], check=True).stdout.splitlines()
        body = generate_pr_body(branch, commits)
        if remote_branch_exists:
            print('📤 Пушу локальні зміни до origin...')
            run_git_command(['git', 'push', 'origin', branch], check=True)

        if owner and repo and os.environ.get('GITHUB_TOKEN'):
            token = os.environ['GITHUB_TOKEN']
            existing_pr = find_existing_pr(owner, repo, branch, token)
            if existing_pr:
                print(f'✅ Відкритий PR вже існує: {existing_pr["html_url"]}')
                return 0

            print('🚀 Створюю GitHub pull request...')
            pr = create_pull_request(owner, repo, default_branch, branch, title, body, token)
            print(f'✅ Pull request створено: {pr["html_url"]}')
            return 0

        compare_url = f'https://github.com/{owner}/{repo}/compare/{default_branch}...{branch}?expand=1'
        print('⚠️ GitHub PR creation skipped. Set GITHUB_TOKEN to create automatically.')
        print(f'📝 Use this URL to open a pull request manually: {compare_url}')
        print(f'PR title suggestion: {title}')
        print('PR body suggestion:')
        print(body)
        return 0

    except subprocess.CalledProcessError as err:
        print('❌ Помилка Git:', err.stderr.strip() or err.stdout.strip())
        return 1
    except Exception as err:
        print('❌ Помилка:', str(err))
        return 1


if __name__ == '__main__':
    sys.exit(main())
```

> Це автономний скрипт. Він не запитує у користувача додаткових даних під час виконання.
