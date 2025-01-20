import subprocess

subprocess.run(["pip3", "install", "termcolor"], shell=True, capture_output=True)
subprocess.run(["winget", "install", "ngrok"], shell=True, capture_output=True)

print("\nDependencies installed (:")
