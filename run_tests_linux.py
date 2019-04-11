import subprocess
from subprocess import *
import os
dir = os.listdir()
from subprocess import Popen


for file in dir:
    if file.startswith("Chatbot"):
        os.chdir(file)
        testsh = open("test.sh","w+")
        testsh.write("#!/bin/bash\n")
        testsh.write("\n")
        testsh.write("# Entrainement 1\n")
        testsh.write("python3 ~/chatbot/Libs/Python/End2end_maker.py\n")
        testsh.write("python3 -m rasa_core.evaluate default --core models/dialogue --nlu models/current/nlu --stories e2e_stories.md --e2e\n")
        testsh.write("python3 ~/chatbot/Libs/Python/Score_reader.py\n")
        testsh.close()
        os.system("chmod 777 test.sh")
        os.system("gnome-terminal -e ./test.sh --title="+file+"-test")

        os.chdir("..")
