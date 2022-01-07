import csv
from collections import Counter

def getmean(totalweight, totalentries):
    mean = totalweight/totalentries
    print(mean)

def getmedian(totalentries, sorteddata):
    if totalentries % 2 == 0:
        median1 = float(sorteddata[totalentries//2])
        median2 = float(sorteddata[totalentries//2-1])
        median = (median1 + median2)/2
    else:
        median = float(sorteddata[totalentries//2])
    print(median)

def getmode(sorteddata):
    data = Counter(sorteddata)

    moderange = {
        "75-85" : 0,
        "85-95" : 0,
        "95-105" : 0,
        "105-115" : 0,
        "115-125" : 0,
        "125-135" : 0,
        "135-145" : 0,
        "145-155" : 0,
        "155-165" : 0,
        "165-175" : 0,
    }
    for weight,occurence in data.items():
        if 75 < weight < 85:
            moderange["75-85"] += occurence
        elif 85 < weight < 95:
            moderange["85-95"] += occurence
        elif 95 < weight < 105:
            moderange["95-105"] += occurence
        elif 105 < weight < 115:
            moderange["105-115"] += occurence
        elif 115 < weight < 125:
            moderange["115-125"] += occurence
        elif 125 < weight < 135:
            moderange["125-135"] += occurence
        elif 135 < weight < 145:
            moderange["135-145"] += occurence
        elif 145 < weight < 155:
            moderange["145-155"] += occurence
        elif 155 < weight < 165:
            moderange["155-165"] += occurence
        elif 165 < weight < 175:
            moderange["165-175"] += occurence
    
    modedata, modeoccurence = 0,0

    for range,occurence in moderange.items():
        if occurence > modeoccurence:
            modedata, modeoccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

    mode = float((modedata[0] + modedata[1])/2)

    print(mode)

with open("C:/Users/Jonathan Wu/Downloads/White Hat/New folder/SOCR-HeightWeight.csv", newline = '') as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)

totalweight = 0
totalentries = len(filedata)
sorteddata = []

for persondata in filedata:
    totalweight += float(persondata[2])
    sorteddata.append(float(persondata[2]))

sorteddata.sort()

getmean(totalweight, totalentries)

getmedian(totalentries, sorteddata)

getmode(sorteddata)