# R E V I S, a tool used to hack victims using python.

import time
import socket
import reversed

def main():

	options = input("""
R e v i s
	"Hacking made easy"

1); Generate Payload 
2); Hack Victim.  



>>  """)

	if options == "1":
		reversed.payloadSelection()
	elif options == "2":
		pass
	else:
		print("Select using 1 or 2. ")
		time.sleep(2)
		main()


main()