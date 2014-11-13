import os
import shutil
import re
import csv


rootDir = 'C:/Users/Bisakha Ray/Desktop/mimic2cdb-2.6-00(1)/'
username = 'NEWBORN'

for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
       if fname.startswith('DEMOGRAPHIC_DETAIL'):
       #print('\t%s' % fname)
       #src = dirName+'/'+fname
         with open(dirName+'/'+fname, 'rt') as f:
           reader = csv.reader(f, delimiter=',') # good point by @paco
           flag = 0
           for row in reader:
             for field in row:
               if field == username:
                  print "is in file"
                  flag = 1
           if flag == 0:
               extension = fname.split('-')[1]
               src = dirName+'/'+'NOTEEVENTS-'+extension
               dest = 'C:/Users/Bisakha Ray/Desktop/YIN/DischargeSummaries_filtered/'+'NOTEEVENTS-'+extension

               f = open(src)
               f1 = open(dest, 'a')

               for line in f.readlines():
                    f1.write(line)   

               f1.close()
               f.close()
