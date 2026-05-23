# Skill: Auto Git Pull and Sync

This skill is a self-contained Python helper that automatically detects the current Git repository, fetches from `origin`, and pulls the current branch without asking for interactive input.

```python
import os
import subprocess
import sys


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
        remotes = run_git_command(['git', 'remote'], check=True).stdout.splitlines()
        if 'origin' not in remotes:
            print('❌ Віддалений репозиторій origin не знайдено.')
            return 1

        print('🌐 Отримую оновлення з origin...')
        run_git_command(['git', 'fetch', 'origin'], check=True)

        print('⬇️ Пулю поточну гілку...')
        run_git_command(['git', 'pull', '--ff-only', 'origin', branch], check=True)

        print('✅ Синхронізація завершена. Поточна гілка оновлена.')
        return 0

    except subprocess.CalledProcessError as err:
        print('❌ Помилка Git:', err.stderr.strip() or err.stdout.strip())
        return 1


if __name__ == '__main__':
    sys.exit(main())
```

> Це автономний скрипт. Він не запитує у користувача додаткових даних під час виконання.
