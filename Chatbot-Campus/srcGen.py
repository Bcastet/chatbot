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

	if splitted[0].startswith("/Campus"):
		return (splitted[0].replace("/Campus/",""),htmlLine)
	else:
		return ("False","False")

def parseFile():
	items = {}
	siteMap = open("siteMap.html","r",errors="ignore",encoding="latin1")
	categories=[]
	realCategories={}
	lineChecker=0
	for line in siteMap:

		if lineChecker>=592 and lineChecker<=5360:

			tmp = parseLine(line)
			if tmp!=("False","False"):
				if not(tmp[0].rsplit("/")[0] in categories):
					categories.append(tmp[0].rsplit("/")[0])
					realCategories[tmp[1].encode("latin1").decode("utf8")]=tmp[0]
				items[tmp[1]]=tmp[0]
		lineChecker+=1
	
	return realCategories



def createStories(items):
	storiesmd = open("Stories.md","w")
	for item in items.keys():
		storiesmd.write("## "+item.replace(" ","_")+" path\n")
		storiesmd.write("* "+item.replace(" ","_")+"\n")
		storiesmd.write("  - utter_"+item.replace(" ","_")+"\n\n")
	storiesmd.close()
	storiesmd = open("Stories.md","r")
	filestr=storiesmd.read()
	storiesmd.close()
	storiesmd = open("Stories.md","wb")	
	storiesmd.write(filestr.encode("utf-8"))

def createNlu(items):
#### intent:emploi_du_temps
##- Ou est mon emploi du temps?
	nlumd = open("nlu.md","w+")
	for item in items.keys():

		nlumd.write(("## intent:"+item.replace(" ","_")+"\n"))
		nlumd.write("- "+"Je cherche des informations à propos de "+item.replace("-"," ").lower()+"\n")
		nlumd.write("- "+"Où puis-je trouver les informations concernant "+item.replace("-"," ").lower()+"?\n")
		nlumd.write("- "+"Je cherche le portail "+item.replace("-"," ").lower()+"\n\n")
		

	
	nlumd.close()
	nlumd = open("nlu.md","r")
	filestr=nlumd.read()
	nlumd.close()
	nlumd = open("nlu.md","wb")	
	nlumd.write(filestr.encode("utf-8-sig"))
	nlumd.close()
	nlumd = open("nlu.md",encoding="utf-8-sig")
	


def createDomain(items):
	domainyml = open("domain.yml","w+")
	domainyml.write("intents:\n")

	for item in items.keys():
		
		domainyml.write("  - "+item.replace(" ","_")+"\n")

	domainyml.write("\n"+"actions:\n")

	for item in items.keys():
		
		domainyml.write("- utter_"+item.replace(" ","_")+"\n")

	domainyml.write("\ntemplates:\n")

	for item in items.keys():
		
		domainyml.write("  utter_"+(item.replace(" ","_"))+":\n")
		it = str(item.lower())
		towrite = "    - \"Les informations concernant le/la "+it+" de l'université sont à cette page : https://www.u-bordeaux.fr/Campus/"+items[item]+"     \"\n\n"
		domainyml.write(towrite)
	domainyml.close()
	domainyml = open("domain.yml","r")
	filestr=domainyml.read()
	domainyml.close()
	domainyml = open("domain.yml","wb")
	
	domainyml.write(filestr.encode("utf-8-sig"))


items = parseFile()
items.pop('Campus')
items.pop("Tous les événements de la rentrée 2015")

createDomain(items)
createStories(items)
createNlu(items)
print("Chatbot generated")

