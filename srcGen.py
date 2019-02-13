def parseLine(htmlLine):
	try:
		htmlLine.replace("<li><a href=","")
	
		quote=0
		splitted = htmlLine.rsplit("\">")

		print(splitted)
		htmlLine = splitted[1]
		htmlLine = htmlLine.rsplit("<")[0]
		splitted[0]=splitted[0].rsplit("\"")[1]
	except Exception as e:
		return ("False","False")

	
	return (splitted[0],htmlLine)

def parseFile():
	items = {}
	siteMap = open("siteMap.html","r",errors="ignore")
	 
	lineChecker=0
	for line in siteMap:
		
		if lineChecker>=596 and lineChecker<=5360:
			print(lineChecker)
			tmp = parseLine(line)
			if tmp!=("False","False"):
				items[tmp[1]]=tmp[0]
				print(tmp)
				
			
			
		lineChecker+=1

	return items



def createStories(items):
  storiesmd = open("Stories1.md","w+")
  for item in items.keys():
  	storiesmd.write("## "+item.replace(" ","_")+" path\n")
  	storiesmd.write("* "+item.replace(" ","_")+"\n")
  	storiesmd.write("  - utter_"+item.replace(" ","_")+"\n\n")
  storiesmd.close()

def createNlu(items):
#### intent:emploi_du_temps
##- Ou est mon emploi du temps?
	nlumd = open("nlu1.md","w+")
	for item in items.keys():
		nlumd.write("## intent:"+item+"\n")
		nlumd.write("-"+item+"\n\n")
	nlumd.close()


def createDomain(items):
	domainyml = open("domain1.yml","w+")
	domainyml.write("intents:\n\n")

	for item in items.keys():
		domainyml.write("  - "+item.replace(" ","_")+"\n")

	domainyml.write("\n"+"actions:\n\n")

	for item in items.keys():
		domainyml.write("- utter_"+item.replace(" ","_")+"\n")

	domainyml.write("\ntemplates:\n")

	for item in items.keys():
		domainyml.write("- utter_"+item.replace(" ","_")+":\n")
		domainyml.write("  - text: "+"\"Vous pouvez trouver les renseignements a propos de "+ item +"https://www.u-bordeaux.fr"+items[item]+"\"\n\n")

items = parseFile()
createStories(items)
createNlu(items)
createDomain(items)

	



