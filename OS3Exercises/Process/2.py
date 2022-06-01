def processlist ():
    file = open("process.txt", "r")
    data = file.readlines()
    rootlist = []
    userlist = []
    
    idx1 = 0
    idx2 = 0
    
    for line in data:
        if 'root' in line:
            rootlist.insert(idx1, line)
            idx1 += 1
        elif 'delano' in line:
            userlist.insert(idx2, line)
            idx2 += 1
     
    file.close()
    
    lineLen1 = len(rootlist)
    lineLen2 = len(userlist)
    for i in range (lineLen1):
        print(end = rootlist[i])
    
    for i in range (lineLen2):
        print(end = userlist[1])
        
processlist()
