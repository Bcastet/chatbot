nb_stories = 0
line_number = 0
with open("e2e_stories.md","w") as e2e_stories:
    with open('qa.txt',"r") as f:
        for line in f:
            if line_number%2==0:
                e2e_stories.write("## end-to-end story "+str(nb_stories)+"\n")
                e2e_stories.write("* inform: "+line)
                nb_stories+=1
            else:
                e2e_stories.write("   - utter_"+line+"\n")
                e2e_stories.write('\n')
            line_number+=1
print("Generated e2e_stories.md")
