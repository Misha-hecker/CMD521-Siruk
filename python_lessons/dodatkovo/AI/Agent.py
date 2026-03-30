import os
import asyncio
from openai import OpenAI

# SETTINGS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_FILE = os.path.join(BASE_DIR, "prompt.txt")
ROOT = os.path.join(BASE_DIR, "ai_folder")

# Create folder if it does not exist
os.makedirs(ROOT, exist_ok=True)

# Connect to LM Studio
ai = OpenAI(base_url="http://localhost:1234/v1", api_key="lm")

def get_instructions():
    """Read prompt.txt or use a simple default."""
    if os.path.exists(PROMPT_FILE):
        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "You are a terminal assistant."

async def run_command(cmd):
    """Run command inside ai_folder."""
    process = await asyncio.create_subprocess_shell(
        f"cd {ROOT} && {cmd}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (stdout.decode() or stderr.decode()).strip()

async def main():
    print(f"🚀 Agent started.")
    print(f"📁 Folder: {ROOT}")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("👤 You: ")
        
        if user_input.lower() in ["exit", "quit", "stop"]:
            print("👋 Bye!")
            break

        # Get fresh list of files
        files = os.listdir(ROOT)
        instructions = get_instructions()
        
        # Simple system prompt
        system_prompt = (
            f"{instructions}\n\n"
            f"Your folder: {ROOT}\n"
            f"Files: {files}\n"
            "Write commands like this: [CMD] command. Be short."
        )

        try:
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(None, lambda: ai.chat.completions.create(
                model="qwen-2.5-7b-instruct",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            ))
            
            res = response.choices[0].message.content

            if "[CMD]" in res:
                # Parse and run command
                cmd = res.split("[CMD]")[1].split('\n')[0].strip()
                print(f"💻 Running: {cmd}")
                
                out = await run_command(cmd)
                
                if out:
                    # Show only first 500 characters
                    display_out = out if len(out) < 500 else out[:500] + "..."
                    print(f"📝 Result:\n{display_out}")
                else:
                    print("✅ Done.")
            else:
                print(f"🤖 AI: {res}")

        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExit...")