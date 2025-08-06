# R e v i s
![image](https://github.com/user-attachments/assets/40f4321c-e40a-4fd8-bd2c-c8ad04903004)

# Setup steps for R e v i s automated.  

1. Navigate over to ngrok.com
2. make an account, grab your auth token
3. Install then add the executable to the PATH, C:\Windows\System32
4. run "ngrok config add-authtoken <auth token>" in a command prompt
5. all done.

# Installation
if the requirements.py doesn't work then you'll have to do a manual installation, please refer to the bold text below: 

**pip3 install termcolor**

after you will need to head over to ngrok.com, download the portable executable then copy it to your windows PATH directory.

# Information
This is a tool you can effectively use get into another computer remotely, the tool utilizes TCP sockets to send and recieve 
data via a process that pipes standard input and output through the socket and onto your computers screen.

Whether it be locally, over the internet.. this tool aims to provide some automation and simplicity with regards to executing reverse shells.
