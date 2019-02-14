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

	if splitted[1]!="\n":
		return (splitted[0],htmlLine)
	else:
		return ("False","False")

def parseFile():
	items = {}
	siteMap = open("siteMap.html","r")
	 
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
  #storiesmd.write("## Portes_ouverte path\n")
  #storiesmd.write("* Portes_ouverte\n")
  #storiesmd.write("  - utter_Portes_ouverte\n")
  #storiesmd.write("")
  for item in items.keys():
  	
	  	rewrittenItem = item.replace(" ","_")
	  	rewrittenItem = rewrittenItem.replace(",","")
	  	rewrittenItem = rewrittenItem.replace(":","")
	  	rewrittenItem = rewrittenItem.replace("\"","")
	  	rewrittenItem = rewrittenItem.replace("/","")
	  	storiesmd.write("## "+rewrittenItem+" path\n")
	  	storiesmd.write("* "+rewrittenItem+"\n")
	  	storiesmd.write("  - utter_"+rewrittenItem+"\n\n")
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
		rewrittenItem=item.replace(" ","_")
		rewrittenItem=rewrittenItem.replace("!","")
		domainyml.write("  - "+rewrittenItem+"\n")

	domainyml.write("\n"+"actions:\n\n")

	for item in items.keys():
		domainyml.write("- utter_"+item.replace(" ","_")+"\n")

	domainyml.write("\ntemplates:\n")

	for item in items.keys():
		domainyml.write("- utter_"+(item.replace(" ","_")).replace("\"","")+":\n")
		if items[item].startswith("/Actualites"):
			domainyml.write("  - text: "+"\"Vous pouvez trouver l'article \\\""+ item.replace("\"","") +"\\\" ici : https://www.u-bordeaux.fr"+items[item]+"\"\n\n")
		else:
			domainyml.write("  - text: "+"\"Vous pouvez trouver les renseignements a propos de "+ item.replace("\"","") +" ici : https://www.u-bordeaux.fr"+items[item]+"\"\n\n")

items = parseFile()
createStories(items)
createNlu(items)
createDomain(items)

	



