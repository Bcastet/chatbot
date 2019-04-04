import subprocess
from subprocess import *
import os 
dir = os.listdir()
from subprocess import Popen


 #Windows

# run in parallel

# do other things here..
# wait for completion

for file in dir:
	if file.startswith("Chatbot"):
		os.chdir(file)
		result = subprocess.check_output("python srcGen.py")
		
		if result.decode().startswith("Chatbot generated"):
			print(file +" sources were successfully generated.")
		else:
			print("Error while generating "+file)
		os.system("start cmd /K chatbot.cmd")
		os.chdir("..")