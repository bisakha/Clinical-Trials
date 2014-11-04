# Import the os module, for the os.walk function
import os
import shutil
 
# Set the directory you want to start from
rootDir = 'C:/Users/Bisakha Ray/Desktop/YIN/DischargeSummaries/'
dest = 'C:/Users/Bisakha Ray/Desktop/YIN/Discharge_Summaries.csv'

for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found file: %s' % fileList)
    for fname in fileList:
       
           print('\t%s' % fname)
           src = dirName+'/'+fname
           
           f = open(src)
           f1 = open(dest, 'a')

           for line in f.readlines():
               f1.write(line)   

           f1.close()
           f.close()
