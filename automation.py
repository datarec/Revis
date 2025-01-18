import subprocess
from termcolor import colored
import threading

def start_ngrok_service():
    subprocess.CREATE_NEW_CONSOLE
    #process = subprocess.Popen(["ngrok", "tcp", "3443"], 
    #                           shell=True,)


def clear_screen():
    subprocess.run(["cls"], shell=True)


def main():
    clear_screen()
    start_ngrok_service()


if __name__ == "__main__":
    main()
