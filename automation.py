import subprocess
from termcolor import colored
import threading

def start_ngrok_service():
    NEW_CONSOLE = subprocess.CREATE_NEW_CONSOLE
    subprocess.Popen(
                    ["ngrok", "tcp", "3333"], 
                     creationflags=NEW_CONSOLE
    )
    subprocess.Popen(
                    ["python", "main.py"] 
    )


def clear_screen():
    subprocess.run(["cls"], shell=True)


def main():
    clear_screen()
    start_ngrok_service()


if __name__ == "__main__":
    main()
