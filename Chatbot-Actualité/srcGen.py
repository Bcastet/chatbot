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

	if splitted[1]!="\n" and splitted[0].startswith("/Actualites"):
		return (splitted[0].replace("/Actualites/",""),htmlLine)
	else:
		return ("False","False")

def parseFile():
	items = {}
	siteMap = open("siteMap.html","r",errors="ignore")
	categories=[]
	realCategories={}
	lineChecker=0
	for line in siteMap:

		if lineChecker>=592 and lineChecker<=5360:

			tmp = parseLine(line)
			if tmp!=("False","False"):
				if not(tmp[0].rsplit("/")[0] in categories):
					categories.append(tmp[0].rsplit("/")[0])
					realCategories[tmp[1]]=tmp[0]
				items[tmp[1]]=tmp[0]
		lineChecker+=1

	return realCategories



def createStories(items):
  storiesmd = open("Stories.md","w")
  #storiesmd.write("## Portes_ouverte path\n")
  #storiesmd.write("* Portes_ouverte\n")
  #storiesmd.write("  - utter_Portes_ouverte\n")
  #storiesmd.write("")
  for item in items.keys():

	  	storiesmd.write("## "+item.replace(" ","_")+" path\n")
	  	storiesmd.write("* "+item.replace(" ","_")+"\n")
	  	storiesmd.write("  - utter_"+item.replace(" ","_")+"\n\n")
  storiesmd.close()

def createNlu(items):
#### intent:emploi_du_temps
##- Ou est mon emploi du temps?
	nlumd = open("nlu.md","w+")
	for item in items.keys():


		nlumd.write(("## intent:"+item.replace(" ","_")+"\n"))
		nlumd.write("- "+"Je cherche des articles à propos "+item.replace("-"," ").lower()+"\n")
		nlumd.write("- "+"Quelles sont les dernières informations à propos "+item.replace("-"," ").lower()+"?\n")
		nlumd.write("- "+"Quelles sont les dernières actualités à propos "+item.replace("-"," ").lower()+"?\n")
		nlumd.write("- "+"Je cherche les dernières nouvelles à propos "+item.replace("-"," ").lower()+"\n\n")


	nlumd.close()
	nlumd = open("nlu.md","r")
	filestr=nlumd.read()
	nlumd.close()
	nlumd = open("nlu.md","wb")

	nlumd.write(filestr.encode("utf-8-sig"))



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

		towrite = "    - \"Toute l'actualité "+item.replace("D","d")+" se trouve sur cette page : https://www.u-bordeaux.fr/Actualites?category="+items[item]+"\"\n"

		domainyml.write(towrite)


items = parseFile()
createDomain(items)
createStories(items)
createNlu(items)
print("Chatbot generated")
