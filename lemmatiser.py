import os

def isSingular(word):
    print("Inside isSIngular")
    inputFile=open("./telugu.input.txt",'w',encoding='utf-8')
    outputFile=open("./telugu.output.txt",'r',encoding='utf-8')
    inputFile.write(word)
    inputFile.close()
    os.system('make tag -sC \'.\'')
    wordDetails = outputFile.readline()
    if  ('sg' in wordDetails) :
        return(True)
    else:
        False


import re

sunna = "ం"
lu = "లు"
chi = "చి"
gaa = "గా"
lo = "లో"
lni = "ల్ని"
che = "చే"
nu = "ను"
du = "డు"
ni = "ని"
tho = "తో"
mdhi = "ంది"
sthu = "స్తూ"
na = "న"
aithvam = "ై"
ki = "కి"


def Lemmatizer(word):
    newSuffix = ""
    rootForm = word
    print("Inside Lemmatizer: ", word)
    previouslyMatched = "No"

    if (len(word) >= 1 and word[-1] == sunna):
        print("Inside 1")
        if (len(word) >= 5):
            if (word[-5:] == "కోవటం"):
                newSuffix = "కొను"
                rootForm = word[:-5] + newSuffix
                previouslyMatched = "Yes"

            elif (word[-5:] == "పోవడం"):
                newSuffix = "పోవు"
                rootForm = word[:-5] + newSuffix
                previouslyMatched = "Yes"

        if (len(word) >= 3):
            if (word[-3:] == "చడం"):
                newSuffix = "చు"
                rootForm = word[:-3] + newSuffix
                previouslyMatched = "Yes"

        if (len(word) >= 5 and previouslyMatched == "No"):
            if (word[-5:] == "చ్చాం"):
                newSuffix = "చ్చు"
                rootForm = word[:-5] + newSuffix

    #            ================================= END OF THE RULE 1 =============================

    elif (len(word) >= 2 and word[-2:] == lu):
        print("Inside 2")
        if (len(word) >= 3):
            if (len(word) >= 5 and word[-5:] == "్నులు"):
                rootForm = word[:-2]
            elif (word[-3:] == "ులు"):
                if (not isSingular(word)):
                    newSuffix = "ి"
                    rootForm = word[:-3] + newSuffix
            elif (word[-3:] == "ాలు"):
                if (not isSingular(word)):
                    newSuffix = "ం"
                    rootForm = word[:-3] + newSuffix
            elif (len(word) > 4 and word[-4:] == "ట్లు"):
                if (not isSingular(word)):
                    newSuffix = "ట్లు"
                    rootForm = word[:-4] + newSuffix
            elif (len(word) > 4 and word[-4:] == "ళ్లు"):
                if (not isSingular(word)):
                    newSuffix = "లు"
                    rootForm = word[:-4] + newSuffix
            elif (word[-3:] == "్లు"):
                newSuffix = "ు"
                rootForm = word[:-3] + newSuffix
            elif (not isSingular(word)):
                rootForm = word[:-2]


    #            ================================= END OF THE RULE 2 =============================

    elif (len(word) >= 2 and word[-2:] == chi):
        print("Inside 3")
        if (len(word) >= 3 and word[-3:] == "చి"):
            newSuffix = "ుచు"
            rootForm = word[:-3] + newSuffix
        else:
            newSuffix = "చు"
            rootForm = word[:-2] + newSuffix

    #            ================================= END OF THE RULE 3 =============================

    elif (len(word) >= 2 and word[-2:] == gaa):
        print("Inside 4")
        if (len(word) >= 4):
            if (word[-4:] == "లుగా"):
                newSuffix = "లు"
                rootForm = word[:-2]
                rootForm = Lemmatizer(rootForm)
            elif (word[-4:] == "లాగా"):
                rootForm = word[:-4]
            elif (word[-4:] == "గ్గా"):
                newSuffix = "కు"
                rootForm = word[:-4] + newSuffix
            elif (word[-4:] == "లోగా"):
                newSuffix = "లో"
                rootForm = word[:-4] + newSuffix
                rootForm = Lemmatizer(rootForm)
            else:
                rootForm = word[:-2]

    #            ================================= END OF THE RULE 4 =============================

    elif (len(word) >= 2 and word[-2:] == lo):
        print("Inside 5")
        if (len(word) >= 7):
            if (word[-7:] == "ళ్లల్లో"):
                newSuffix = "ళ్లు"
                previouslyMatched = "Yes"
            elif (word[-7:] == "ళ్ళల్లో"):
                newSuffix = "ళ్ళు"
                previouslyMatched = "Yes"
            rootForm = word[:-7] + newSuffix
        if (len(word) >= 6 and word[-6:] == "్లల్లో"):
            rootForm = word[:-4]
            if (not isSingular(rootForm)):
                print("Inside lo subrule: ", rootForm)
                newSuffix = "ు"
                rootForm = rootForm + newSuffix
                rootForm = Lemmatizer(rootForm)
                previouslyMatched = "Yes"
        if (previouslyMatched == "No" and len(word) >= 4 and word[-4:] == "ల్లో"):
            newSuffix = "లు"
            rootForm = word[:-4] + newSuffix
            previouslyMatched = "Yes"
        if (previouslyMatched == "No" and len(word) >= 3 and word[-3:] == "లలో"):
            newSuffix = "లు"
            rootForm = word[:-3] + newSuffix
            if (not isSingular(rootForm)):
                rootForm = Lemmatizer(rootForm)
            previouslyMatched = "Yes"
        if (previouslyMatched == "No"):
            rootForm = word[:-2]

    #            ================================= END OF THE RULE 5 =============================

    elif (len(word) >= 4 and word[-4:] == lni):
        print("Inside 6")
        if (len(word) >= 5):
            if (word[-5:] == "ాల్ని"):
                newSuffix = "ం"
                previouslyMatched = "Yes"
            elif (word[-5:] == "ుల్ని"):
                newSuffix = "ి"
                previouslyMatched = "Yes"
            rootForm = word[:-5] + newSuffix
        if (previouslyMatched == "No"):
            rootForm = word[:-4]

    #            ================================= END OF THE RULE 6 =============================

    elif (len(word) >= 2 and word[-2:] == che):
        print("Inside 7")
        if (len(word) >= 3):
            if (word[-3:] == "ిచే"):
                newSuffix = "ుచు"
                rootForm = word[:-3] + newSuffix
            else:
                newSuffix = "ు"
                rootForm = word[:-1] + newSuffix

    #            ================================= END OF THE RULE 7 =============================

    elif (len(word) >= 2 and word[-2:] == nu):
        print("Inside 8")
        if (len(word) >= 6 and word[-6:] == "స్తాను"):
            newSuffix = "ంచు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 5 and word[-5:] == "డతాను"):
            newSuffix = "ట్టు"
            rootForm = word[:-5] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "తాను"):
            newSuffix = ""
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "యాను"):
            newSuffix = "వు"
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 6 and word[-6:] == "న్నాను"):
            newSuffix = "న్ను"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 6 and re.search(".*ి.ాను$", word)):
            newSuffix = word[-6] + "ు" + word[-4] + "ు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 3 and word[-3:] == "ాను"):
            newSuffix = "ు"
            rootForm = word[:-3] + newSuffix
        elif (len(word) >= 3 and word[-3:] == "లను"):
            newSuffix = "లు"
            rootForm = word[:-3] + newSuffix
            if (not isSingular(rootForm)):
                rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 5 and word[-5:] == "నన్ను"):
            rootForm = word
        else:
            rootForm = word[:-2]

    #            ================================= END OF THE RULE 8 =============================

    elif (len(word) >= 2 and word[-2:] == du):
        print("Inside 9")
        if (len(word) >= 6 and re.search(".*ి.ాడు$", word)):
            newSuffix = word[-6] + "ు" + word[-4] + "ు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 5 and word[-5:] == "్నాడు"):
            newSuffix = "ను"
            rootForm = word[:-5] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "తాడు"):
            rootForm = word[:-5]
        elif (len(word) >= 4 and word[-4:] == "యాడు"):
            newSuffix = "వు"
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "శాడు"):
            newSuffix = "యు"
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 6 and word[-6:] == "డ్డాడు"):
            newSuffix = "డు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 3 and word[-3:] == "ాడు"):
            newSuffix = "ు"
            rootForm = word[:-3] + newSuffix
        elif (len(word) >= 6 and re.search(".*ి.ేడు$", word)):
            newSuffix = word[-6] + "ు" + word[-4] + "ు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 3 and word[-3:] == "ేడు"):
            newSuffix = "ు"
            rootForm = word[:-3] + newSuffix

    #            ================================= END OF THE RULE 9 =============================

    elif (len(word) >= 2 and word[-2:] == ni):
        print("Inside 10")
        if (len(word) >= 4 and word[-4:] == "కుని"):
            newSuffix = "కొను"
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 5 and word[-5:] == "ాన్ని"):
            newSuffix = "ం"
            rootForm = word[:-5] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "న్ని"):
            rootForm = word
        elif (len(word) >= 3 and word[-3:] == "్ని"):
            newSuffix = "ు"
            rootForm = word[:-3] + newSuffix
        elif (len(word) >= 6 and word[-6:] == "క్కొని"):
            newSuffix = "గు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 6 and word[-6:] == "క్కొని"):
            newSuffix = "గు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "కుని"):
            newSuffix = ""
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "లోని"):
            newSuffix = "లో"
            rootForm = word[:-4] + newSuffix
            rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 3 and word[-3:] == "లని"):
            newSuffix = "ు"
            rootForm = word[:-2] + newSuffix
            rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 2 and word[-2:] == "ని"):
            newSuffix = ""
            rootForm = word[:-2] + newSuffix


    #            ================================= END OF THE RULE 10 =============================

    elif (len(word) >= 2 and word[-2:] == tho):
        print("Inside 11")
        if (len(word) >= 4 and word[-4:] == "ాలతో"):
            newSuffix = "ాలు"
            rootForm = word[:-4] + newSuffix
            if (not isSingular(rootForm)):
                rootForm = rootForm[:-3]
                rootForm += 'ం'
        elif (len(word) >= 3 and word[-3:] == "లతో"):
            newSuffix = "లు"
            rootForm = word[:-3] + newSuffix
            if (not isSingular):
                rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 4 and word[-4:] == "ల్తో"):
            newSuffix = "లు"
            rootForm = word[:-3] + newSuffix
            if (not isSingular):
                rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 4 and word[-4:] == "త్తో"):
            newSuffix = "తి"
            rootForm = word[:-4] + newSuffix
        else:
            rootForm = word[:-2]


    #            ================================= END OF THE RULE 11 =============================

    elif (len(word) >= 1 and word[-1:] == "ల"):
        print("Inside 12")
        if (not isSingular):
            newSuffix = "ు"
            rootForm = word + newSuffix
            rootForm = Lemmatizer(rootForm)

    #            ================================= END OF THE RULE 12 =============================

    elif (len(word) >= 2 and word[-2:] == "కు"):
        print("Inside 13")
        if (len(word) >= 3 and word[-3:] == "లకు"):
            newSuffix = "లు"
            rootForm = word[:-3] + newSuffix
            if (not isSingular(rootForm)):
                rootForm = Lemmatizer(rootForm)
        else:
            rootForm = word[:-2]

    #            ================================= END OF THE RULE 13 =============================

    elif (len(word) >= 3 and word[-3:] == mdhi):
        print("Inside 14")
        if (len(word) >= 8 and re.search('.+ి.ింది$', word)):
            newSuffix = word[-7] + "ు" + word[-5] + "ు"
            rootForm = word[:-7] + newSuffix
        elif (len(word) >= 6 and word[-6:] == "ేసింది"):
            newSuffix = "ు"
            rootForm = word[:-7] + newSuffix
        elif (len(word) >= 5 and word[-5:] == "యింది"):
            newSuffix = "వు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "ింది"):
            newSuffix = "ు"
            rootForm = word[:-5] + newSuffix
        elif (len(word) >= 5 and word[-5:] == "తుంది"):
            newSuffix = "వు"
            rootForm = word[:-5] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "ొంది"):
            newSuffix = "ను"
            rootForm = word[:-3] + newSuffix


    #            ================================= END OF THE RULE 14 =============================

    elif (len(word) >= 4 and word[-4:] == sthu):
        print("Inside 15")
        if (len(word) >= 5 and word[-5:] == "ుస్తూ"):
            newSuffix = "ుపు"
            rootForm = word[:-5] + newSuffix
            print("Inside Hai 1")
        elif (len(word) >= 5 and word[-5:] == "ూస్తూ"):
            newSuffix = "ూడు"
            rootForm = word[:-5] + newSuffix
            print("Inside Hai 2")
        elif (len(word) >= 5 and word[-5:] == "ిస్తూ"):
            newSuffix = "ించు"
            rootForm = word[:-4] + newSuffix
            print("Inside Hai 3")
        else:
            newSuffix = "యు"
            rootForm = word[:-4] + newSuffix
            print("Inside Hai 4")


    #            ================================= END OF THE RULE 15 =============================

    elif (len(word) >= 1 and word[-1:] == na):
        print("Inside 16")
        if (len(word) >= 6 and re.search('.+ి.ిన$', word)):
            newSuffix = "ు" + word[-3] + "ు"
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 6 and word[-6:] == "ాల్సిన"):
            newSuffix = "ు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 3 and word[-3:] == "సిన"):
            newSuffix = "యు"
            rootForm = word[:-3] + newSuffix
        elif (len(word) >= 3 and word[-3:] == "యిన"):
            newSuffix = "వు"
            rootForm = word[:-3] + newSuffix
        elif (len(word) >= 2 and word[-2:] == "ిన"):
            newSuffix = "ు"
            rootForm = word[:-2] + newSuffix
        elif (len(word) >= 2 and word[-2:] == "ైన"):
            newSuffix = "ు"
            rootForm = word[:-2] + newSuffix
        elif (len(word) >= 2 and word[-2:] == "ున"):
            rootForm = word[:-1]

            #            ================================= END OF THE RULE 16 =============================

    elif (len(word) >= 1 and word[-1:] == aithvam):
        print("Inside 17")
        if (len(word) >= 3 and word[-3:] == "లపై"):
            newSuffix = "ు"
            rootForm = word[:-2] + newSuffix
            rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 2 and word[-2:] == "పై"):
            rootForm = word[:-2]
        elif (len(word) >= 1 and word[-1:] == "ై"):
            newSuffix = "ు"
            rootForm = word[:-1] + newSuffix

            #            ================================= END OF THE RULE 17 =============================


    elif (len(word) >= 2 and word[-2:] == ki):
        print("Inside 18")
        if (len(word) >= 3 and word[-3:] == "లకి"):
            rootForm = word[:-2]
            if (not isSingular):
                rootForm = rootForm + 'ు'
                rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 5 and word[-5:] == "ానికి"):
            newSuffix = "ం"
            rootForm = word[:-5] + newSuffix
            rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 3 and word[-3:] == "ికి"):
            newSuffix = "ు"
            rootForm = word[:-3] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "లోకి"):
            rootForm = word[:-4]
        else:
            rootForm = word[:-2]

            #            ================================= END OF THE RULE 18 =============================

    return (rootForm)

