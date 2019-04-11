import subprocess
from subprocess import *
import os
dir = os.listdir()
from subprocess import Popen


 #Windows

# run in parallel

# do other things here..
# wait for completion
port = 5005
for file in dir:
	if file.startswith("Chatbot"):
		os.chdir(file)

		result = (subprocess.check_output(["python3","srcGen.py"]))

		if result.decode().startswith("Chatbot generated"):
			print(file +" sources were successfully generated.")
		else:
			print("Error while generating "+file)
		os.system("chmod 777 chatbot.sh")
		chatbotsh=open("chatbot.sh","w+")
		chatbotsh.write(
		"#!/bin/bash\n"+

		"# Entrainement 1\n"+
		"python3 -m rasa_core.train -d domain.yml -s Stories.md -o models/dialogue\n"+
		"# Entrainement 2\n"+
		"python3 -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose\n"+
		"# Lancement du bot\n"+
		"python3 -m rasa_core.run -d models/dialogue -u models/current/nlu -p "+str(port))
		chatbotsh.close()
		os.system("gnome-terminal -e ./chatbot.sh --title="+file+"-port-"+str(port))

		print("Launched "+str(file)+" on port "+str(port))
		port+=1
		os.chdir("..")
