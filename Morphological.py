#!/usr/bin/env python
# coding: utf-8

# In[3]:


def morphologicalGenerator(word):

    if(word[-4:] == "చాడు" or word[-4:] == "టాడు" or word[-4:] == "తాడు" or word[-4:] == "నాడు" or
       word[-6:] == "చ్చాడు" or word[-6:] == "న్నాడు" or word[-6:] == "స్తాడు"):
        Gender = "M"
        Num = "Sg"
    elif(word[-3:] == "నది" or word[-5:] == "న్నది" or word[-7:] == "స్తుంది" or word[-5:] == "టుంది" or 
       word[-5:] == "యింది" or word[-5:] == "న్నది" or word[-7:] == "స్తుంది"):
        Gender = "F"
        Num = "Sg"
    elif(word[-4:] == "తారు" or word[-4:] == "దురు" or word[-4:] == "తిరు" or word[-4:] == "చారు" or word[-4:] == "టారు" or
         word[-4:] == "నారు" or word[-6:] == "చ్చారు" or word[-6:] == "న్నారు" or word[-6:] == "స్తారు"):
        Gender = "M&F"
        Num = "Pl"
    elif(word[-4:] == "చావు" or word[-4:] == "నావు" or word[-6:] == "న్నావు" or word[-4:] == "తావు" or word[-4:] == "దువు" or
         word[-6:] == "స్తావు"):
        Gender = "M&F"
        Num = "Sg"
    elif(word[-4:] == "చాను" or word[-6:] == "చ్చును" or word[-4:] == "నాను" or word[-6:] == "న్నాను"
        or word[-4:] == "తాను" or word[-4:] == "దును" or word[-6:] == "స్తాను"):
        Gender = "M&F"
        Num = "Sg"
    elif(word[-4:] == "టాము" or word[-6:] == "న్నాము" or word[-4:] == "తాము" or word[-4:] == "దుము"):
        Gender = "M&F"
        Num = "Pl"
    elif(word[-3:] == "టవి" or word[-3:] == "నవి" or word[-5:] == "న్నవి" or word[-4:] == "తావి" or 
         word[-4:] == "తివి" or word[-6:] == "స్తావి"):
        Gender = "M&F"
        Num = "Pl"
    elif(word[-4:] == "తిమి"):
        Gender = "M&F"
        Num = "Pl"
    elif(word[-4:] == "తిని"):
        Gender = "M&F"
        Num = "Pl"
    elif(word[-6:] == "స్తాము"):
        Gender = "M&F"
        Num = "Pl"
    return Gender,Num


"""# In[10]:


word = "వస్తుంటాడు"
Gender,Num = morphologicalGenerator(word)
print("For the word ",word,", Gender: ",Gender," and Number: ",Num, sep="")


# In[ ]:"""




