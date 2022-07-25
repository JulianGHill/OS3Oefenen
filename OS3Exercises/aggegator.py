import re
import os
import csv
import glob

#Defining directory
dir_path = 'Results' 
#list for filenames
filelist = []

#Print text
print('Parsing experiment result files in current directory... done')

#Make Directory
print('Creating directory "Aggregated"...',end="") 
if os.path.isdir('aggregated'):
    print('done')
else:
    os.mkdir('aggregated')
    print('done')

#list the files
for path in os.listdir(dir_path):
    #check if current path is file
    if os.path.isfile(os.path.join(dir_path, path)):
        filelist.append(path)

def getIP():
    ip_lst = [ip for file in os.listdir(dir_path) for ip in re.findall(r"\b(?:[1-2]?[0-9]{1,2}\.){3}[1-2]?[0-9]{1,2}\B", file)] 
    final_list = list(dict.fromkeys(ip_lst))
    
    #Print IP's
    print('IP addresses encountered:')
    for i in range(len(final_list)):
        print("    - ", final_list[i])
        
    #make reports
    for i in range(len(final_list)):
        with open('aggregated/' + final_list[i] + '.txt', 'w') as f, open(filelist[i], 'w') as v:
            f.write('pings    target    min/avg/max/mdev\n')
            f.write('======================================\n')
           
            
    for x in range (len(final_list)):
        print('Writing combined dataset to "aggregated/"' + final_list[x] + '...  done')
                
    print('Aggregation completed!')
 
getIP()

