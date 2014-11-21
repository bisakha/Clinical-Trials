import os
import shutil
import re
import csv


rootDir = 'C:/Users/Bisakha Ray/Desktop/mimic2cdb-2.6-00(1)/'
username = 'NEWBORN'

count = 0

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
                  flag = 1
           # if not neonate
           if flag == 0:
               extension = fname.split('-')[1]
               src1 = dirName+'/'+'ICUSTAY_DETAIL-'+extension
               if (os.stat(src1)[6] > 0):
                  with open(src1,'r') as f1:
                    lines = f1.readlines()[1:]
                    mylist = [x.split(',') for x in lines]
                    if (float(mylist[0][23]) > 20):
                       # age greater than 20, can be ACS
                        src = dirName+'/'+'NOTEEVENTS-'+extension
                        if (os.stat(src)[6] > 0):
                           print src
                           count = count + 1
                           dest = 'C:/Users/Bisakha Ray/Desktop/YIN/DischargeSummaries_filtered/'+'NOTEEVENTS-'+extension
                           f2 = open(src)
                           f3 = open(dest, 'a')
                           for line in f2.readlines():
                              f3.write(line)
                           f2.close()
                           f3.close()
              
               f.close()
               f1.close()
               print count
