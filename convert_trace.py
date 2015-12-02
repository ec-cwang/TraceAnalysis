#!/usr/bin/python
#-*- coding:utf-8 -*-
from sys import argv


def splitTrace(traceFile):
    f=open(traceFile,"r")
    traceList=f.readlines()#List of Strings, each element is a line
    metaTraceList=[]
    start=0
    for i,line in enumerate(traceList):
        if "Simulation" in line:
            if i==0:
                continue
            #list[first:last] last in not included
            metaTraceList.append(traceList[start:i])
            start=i
    metaTraceList.append(traceList[start:])#Add last part
    f.close()
    return metaTraceList

def extractInfo(operationList):
    # Requires a list which contains the operations per element
    # Returns a tuple containing potentially useful infomation
    goodRes=0#total number of good results
    badRes=0#total number of bad results
    time=[]#time when there is an operation
    tGood=[]#time when there is a good operation
    tBad=[]#time when there is a bad operation
    for line in operationList:
        if "Simulation" in line:
            continue
        who,t,op,res = line.strip().split(" ")
        if res == "OK":
            goodRes+=1
            tGood.append(int(t[1:]))
        if res == "NOK":
            badRes+=1
            tBad.append(int(t[1:]))
        time.append(int(t[1:]))
    return goodRes, badRes, tGood, tBad, time

#sample=metaTraceList[4]
#print info
#print info[1]
#
#print goodRes
#print badRes
#print len(sample)-1
#print goodRes+badRes
#print time
print "Hello!"
print "你好，世界！"

scriptName, typeTest, seqString = argv
print "typeTest is:", typeTest
print "seqString is:", seqString

#str.strip() to remove leading and trailing whitespace characters
# We can use multiple assignment to parse split elements: a,b,c = [1,2,3]

traceFile="simulation_log_standard.txt"
#traceList=f.readlines()#List of Strings, each element is a line
#delimiterNumber=[i for i,line in enumerate(traceList) if "Simulation" in line]
#print delimiterNumber

metaList=splitTrace(traceFile)

# For individual analysis
infoIndiv=extractInfo(open(traceFile,"r").readlines())
#print infoIndiv

# Prepare For global analysis, conversion to 1 line
groupSign=int(typeTest[0])#int, 1 busInc, 2 busBlue, 3 busBlack
typeSign=typeTest[1]#str, V vertical only, M mixed
seqList=seqString.split(",")
print seqList
print groupSign
print typeSign
cdOpList=metaList[seqList.index("cd")]
cdInfo=extractInfo(cdOpList)
ctOpList=metaList[seqList.index("ct")]
ctInfo=extractInfo(ctOpList)
print cdInfo
print ctInfo
cdOpTotal=cdInfo[0]+cdInfo[1]
cdOpGood=cdInfo[0]
ctOpTotal=ctInfo[0]+ctInfo[1]
ctOpGood=ctInfo[0]
print cdOpTotal
print cdOpGood
print ctOpTotal
print ctOpGood
globalInfo=str(groupSign)+"\t"+str(typeSign)+"\t"+str(cdOpTotal)+"\t"+str(cdOpGood)+"\t"+str(ctOpTotal)+"\t"+str(ctOpGood)
globalInfo+="\n"
print globalInfo
#globalFile=open("globalInfo.txt","a")
#globalFile.write(globalInfo)
