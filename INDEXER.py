import os

theList = os.listdir()
theIndexes = os.listdir()

print(theList)

f = open("demofile3.txt", "w")

i = 0
for file in theList:
    theIndexes[i] = i + 1
    f.write("("+str(theIndexes[i])+") ")
    f.write(file)
    f.write("   TAGS: ")
    f.write("\n")
    i += 1

f.close()
