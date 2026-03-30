import subprocess
import os

exe_path = r"D:\Uncrashed.FPV.Drone.Simulator.v2.6\game\Uncrashed.exe"
game_dir = r"D:\Uncrashed.FPV.Drone.Simulator.v2.6\game"

def launch_game():
    try:
        subprocess.Popen([exe_path], cwd=game_dir)
    except Exception as e:
        print(f"Не вдалося запустити гру: {e}")

if __name__ == "__main__":
    launch_game()
