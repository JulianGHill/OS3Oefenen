# There is a directory filled with files that are labled with the date they have been created on.
# Create a program which takes all files and sorts them from old to new and add the text delte to the oldest on output as such:
# 2002-05-12 [Delete]
# 2003-04-01 [Delete]
# 2011-07-10 [Delete]
# 2012-09-13 [Delete]
# 2022-05-05 [Keep]

import os

listOfFiles = os.listdir(path=r'C:\Users\julia\OneDrive\School\OS3\Python\practical-python-master\OS3Exercises\backupfolder')
listOfFiles.sort()
newKeepList = []
newListOfFiles = []
keep = ' [Keep]'
delete = ' [Delete]'

for file in listOfFiles[:-1]:
    newListOfFiles.append(str(file)+delete)

newKeepList.append(str(listOfFiles[-1])+keep)

newListOfFiles.extend(newKeepList)

print(newListOfFiles)