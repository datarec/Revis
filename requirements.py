import subprocess

print("Downloading depedencies, could take a minute.")
subprocess.run(["pip3", "install", "termcolor"], shell=True, capture_output=True)
subprocess.run(["winget", "install", "choco"], shell=True, capture_output=True)
subprocess.run(["choco", "install", "ngrok"], shell=True, capture_output=True)
print("\nDependencies installed!")
