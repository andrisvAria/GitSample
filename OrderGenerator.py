import pandas
from numpy.random import random, randint, normal, shuffle, choice as randchoice

dataq = pandas.read_excel("/default.xlsx")
originalList = dataq.to_dict('records')

doubletarget = False
listok = False
x = 0

#No consecutive stimuli         originalList[i]["Stimuli"] == originalList[i + 1]["Stimuli"]
# no consecutive Disgustings
while not listok:
    for i in range(len(originalList) - 2):
        if (originalList[i]["Stimuli"] == originalList[i + 1]["Stimuli"]== originalList[i + 2]["Stimuli"]) \
                or (originalList[i]["Type"] == originalList[i + 1]["Type"] ==  originalList[i + 2]["Type"] == "Disgusting")\
                or (originalList[i]["Type"] == originalList[i + 1]["Type"] == "Disgusting" and originalList[i]["Category"] == originalList[i + 1]["Category"]=="Odor"):
            doubletarget = True
            break
    if doubletarget == True:
        shuffle(originalList)
        doubletarget = False
    else:
         listok = True



df = pandas.DataFrame(originalList)
df.to_excel("OrderA.xlsx")

#i will just add a comment
