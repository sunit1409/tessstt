f = open('completeList.txt','r')
w = open('ridList.txt','w')

fileNames = f.readlines()
def checkCondition(fileName):
   conditionNumber = 0
   if "_sp2400_33" in fileName:
       conditionNumber +=1
   if "cc2400_001" in fileName:
       conditionNumber +=1
   if "cc2400_014" in fileName:
       conditionNumber +=1
   if "cc2400_032" in fileName:
       conditionNumber +=1
   return conditionNumber
   
for fileName in fileNames:
   conditionNumber = checkCondition(fileName)
   if conditionNumber == 0:
       w.write(fileName)
       
f.close()       
w.close()
