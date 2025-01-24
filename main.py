import time
import socket
import reverse_shell_gen
from termcolor import colored 
import subprocess
import automated

def clear_screen():
	subprocess.run(["cls"], shell=True)

def main():
	clear_screen()
	try:
		options = input(colored("""R e v i s
	Hacking made easy.

1) Generate payload and Hack (Partially automated - Simpler)
2) Generate Payload (Manual - Advanced) 


>>  """, "light_red"))

		if options == "1":
			automated.main()
		elif options == "2":
			reverse_shell_gen.payloadSelection()
		else:
			print(colored("\nSelect using 1 or 2. ", "light_red"))
			time.sleep(2)
			subprocess.run(["cls"], shell=True)
			main()
	except KeyboardInterrupt:
		print(colored("\n\nGood-bye!", "light_red"))


if __name__ == "__main__":
	main()
