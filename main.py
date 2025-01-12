import time
import socket
import reversed

def main():
	try:
		options = input("""
R e v i s
	Hacking made easy.

1) Generate payload and Hack (Partially automated - Simpler)
2) Generate Payload (Manual - Advanced) 


>>  """)

		if options == "1":
			pass
		elif options == "2":
			reversed.payloadSelection()
		else:
			print("Select using 1 or 2. ")
			time.sleep(2)
			main()
	except KeyboardInterrupt:
		print("Good-bye!")


main()
