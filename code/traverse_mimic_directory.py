# Import the os module, for the os.walk function
import os
import shutil
 
# Set the directory you want to start from
rootDir = 'C:/Users/Bisakha Ray/Desktop/mimic2cdb-2.6-00(1)/00/'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        if fname.startswith('NOTEEVENTS'):
           print('\t%s' % fname)
           dest = 'C:/Users/Bisakha Ray/Desktop/YIN/Discharge_Summaries/'+fname
           src = dirName+'/'+fname
           
           f = open(src)
           f1 = open(dest, 'a')

           for line in f.readlines():
               f1.write(line)   

           f1.close()
           f.close()
