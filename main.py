import time
import socket
import reversed
from termcolor import colored 
import subprocess

def main():
	try:
		options = input(colored("""R e v i s
	Hacking made easy.

1) Generate payload and Hack (Partially automated - Simpler)
2) Generate Payload (Manual - Advanced) 


>>  """, "red"))

		if options == "1":
			pass
		elif options == "2":
			reversed.payloadSelection()
		else:
			print("\nSelect using 1 or 2. ")
			time.sleep(2)
			subprocess.run(["cls"], shell=True)
			main()
	except KeyboardInterrupt:
		print(colored("\n\nGood-bye!", "red"))


main()
