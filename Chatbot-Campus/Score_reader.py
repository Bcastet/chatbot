Nb_tests = 0.0
Nb_success = 0.0
with open('results/failed_stories.md') as f:
    for line in f:
        #print ("This line : "+line)
        if line.startswith("    - utter_"):
            if not(line.startswith("    - utter_salutation")):
                if(len(line)<48):
                    print("Passed")
                    Nb_success+=1
                else:

                    print(line)
        else:
            if line.startswith("## end-to-end story"):
                Nb_tests+=1
            else:
                print(line)


print("We have "+str(Nb_tests)+" tests and "+str(Nb_success)+" successes for a ratio of "+str(Nb_success/Nb_tests*100)+"%")
