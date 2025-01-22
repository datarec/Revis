import subprocess
from termcolor import colored
import threading
import socket
import reversed

def start_ngrok_service():
    NEW_CONSOLE = subprocess.CREATE_NEW_CONSOLE
    subprocess.Popen(
                    ["ngrok", "tcp", "4444"], 
                     creationflags=NEW_CONSOLE 
    )

def start_listener():
    try:
        print("""In the Ngrok window look for the socket. 
Should look something like this: 0.tcp.au.ngrok.io:12527""")
        
        input("Enter: ")
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind(("localhost", 4444))
        listener.listen()
        ip, data = listener.accept()
    except KeyboardInterrupt:
        exit()

def clear_screen():
    subprocess.run(["cls"], shell=True)


def main():
    clear_screen()
    sng_service = threading.Thread(target=start_ngrok_service)
    sng_service.start()
    start_listener()


if __name__ == "__main__":
    main()
