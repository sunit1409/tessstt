f = open('completeList.txt','r')
w = open('ridList.txt','w')

fileNames = f.readlines()
def checkCondition(fileName):
   conditionNumber = 0
   if "yolo" in fileName:
       conditionNumber +=1
   return conditionNumber
   
for fileName in fileNames:
   conditionNumber = checkCondition(fileName)
   if conditionNumber == 0:
       w.write(fileName)
       
f.close()       
w.close()
