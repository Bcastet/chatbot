import sys
import os
import time
def parseLine(htmlLine):
	try:
		htmlLine.replace("<li><a href=","")

		quote=0
		splitted = htmlLine.rsplit("\">")


		htmlLine = splitted[1]
		htmlLine = htmlLine.rsplit("<")[0]
		splitted[0]=splitted[0].rsplit("\"")[1]
	except Exception as e:
		return ("False","False")

	if splitted[1]!="\n" and splitted[0].startswith("/International"):
		return (splitted[0].replace("/International/",""),htmlLine)
	else:
		return ("False","False")

def startswithEvent(str):
	return not(str.startswith("International"))

def parseFile():
	items = {}
	siteMap = open("siteMap.html","r",errors="ignore")
	categories=[]
	realCategories=[]
	lineChecker=0
	for line in siteMap:

		if lineChecker>=592 and lineChecker<=5360:

			tmp = parseLine(line)
			if tmp!=("False","False"):
				if not(tmp[0].rsplit("/")[0] in categories):
					categories.append(tmp[0].rsplit("/")[0])
					realCategories.append(tmp[1])

				items[tmp[1]]=tmp[0]





		lineChecker+=1
	realCategories = list(filter(startswithEvent,realCategories))
	
	return realCategories



def createStories(items):
  storiesmd = open("Stories.md","w")
  #storiesmd.write("## Portes_ouverte path\n")
  #storiesmd.write("* Portes_ouverte\n")
  #storiesmd.write("  - utter_Portes_ouverte\n")
  #storiesmd.write("")
  for item in items:


	  	storiesmd.write("## "+item.replace(" ","_")+" path\n")
	  	storiesmd.write("* "+item.replace(" ","_")+"\n")
	  	storiesmd.write("  - utter_"+item.replace(" ","_")+"\n\n")
  storiesmd.close()

def createNlu(items):
#### intent:emploi_du_temps
##- Ou est mon emploi du temps?
	nlumd = open("nlu.md","w")
	for item in items:
		nlumd.write("## intent : "+item.replace(" ","_")+"\n")
		nlumd.write("- "+"Je cherche des articles a propos "+item.replace("-"," ").lower()+"\n")
		nlumd.write("- "+"Je cherche des informations a propos "+item.replace("-"," ").lower()+"\n")
		nlumd.write("- "+item.replace("-"," ").lower()+"\n\n")
	nlumd.close()


def createDomain(items):
	domainyml = open("domain.yml","w")
	domainyml.write("intents:\n\n")

	for item in items:

		domainyml.write("  - "+item.replace(" ","_")+"\n")

	domainyml.write("\n"+"actions:\n\n")

	for item in items:
		domainyml.write("- utter_"+item.replace(" ","_")+"\n")

	domainyml.write("\ntemplates:\n")

	for item in items:
		domainyml.write("- utter_"+(item.replace(" ","_")).replace("\"","")+":\n")
		domainyml.write("  - text: \"Les renseignements sur le.s "+item.replace("-"," ").lower()+" se trouvent ici: https://u-bordeaux.fr/International/"+item.replace(" ","-")+"\"\n")
items = parseFile()
print(items)
createStories(items)
createNlu(items)
createDomain(items)