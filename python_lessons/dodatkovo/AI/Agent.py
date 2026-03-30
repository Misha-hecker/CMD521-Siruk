import os
import asyncio
from openai import OpenAI

#Configuration vays
# prompt лежить в папці AI, а працювати має в AI/ai_folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
ROOT = os.path.join(BASE_DIR, "ai_folder")

#Make folder if not exist
os.makedirs(ROOT, exist_ok=True)

#Agent Lm Studio
ai = OpenAI(base_url="http://localhost:1234/v1", api_key="lm")

async def run_command(cmd):
    """Виконує системну команду СУВОРО в межах ROOT."""
    process = await asyncio.create_subprocess_shell(
        f"cd {ROOT} && {cmd}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (stdout.decode() or stderr.decode()).strip()

async def main():
    print(f"🚀 Агент активований.")
    print(f"📁 Робоча зона обмежена папкою: {ROOT}")
    print("Введіть 'exit', щоб вийти.\n")

    while True:
        user_input = input("👤 Ви: ")
        
        if user_input.lower() in ["exit", "quit", "вихід"]:
            print("👋 Бувай!")
            break

        files = os.listdir(ROOT)
        
        system_prompt = (
            f"Ти — термінальний помічник. Твоя робоча директорія: {ROOT}. "
            f"Файли в ній: {files}. "
            "Команди пиши СУВОРО у форматі: [CMD] команда. "
            "Не намагайся виходити за межі цієї папки. Відповідай коротко."
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
                cmd = res.split("[CMD]")[1].split('\n')[0].strip()
                print(f"💻 Виконую: {cmd}")
                
                out = await run_command(cmd)
                
                if out:
                    display_out = out if len(out) < 500 else out[:500] + "..."
                    print(f"📝 Результат:\n{display_out}")
                else:
                    print("✅ Виконано.")
            else:
                print(f"🤖: {res}")

        except Exception as e:
            print(f"❌ Помилка зв'язку з LM Studio: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nВихід...")