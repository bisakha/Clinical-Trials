# Import the os module, for the os.walk function
import os
import shutil
import itertools
import re
 
# Set the directory you want to start from
rootDir = 'C:/Users/Bisakha Ray/Desktop/YIN/DischargeSummaries_filtered/'
dest_folder = 'C:/Users/Bisakha Ray/Desktop/YIN/Retrieved/'
count = 0

for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found file: %s' % fileList)
    for fname in fileList:
       
           #print('\t%s' % fname)
           
           src = dirName+'/'+fname
           #file1 = set(line.strip() for line in open(src))
           file1 =(open(src).readline().strip())
           for i in range(1, 398):
            
            dest = dest_folder + str(i) +'.txt'
            file2 = set(line.strip() for line in open(dest))
            
            flag = 0
            #for line in file1 & file2:
            #   if line:
            #       flag = 1
            if file1 in file2:
                flag = 1
            if flag:
               #print fname
               #print i
               count = count + 1
               extension = fname.split("-")
               extension_1 = extension[1].split(".")
               dirname_1 = 'C:/Users/Bisakha Ray/Desktop/YIN/mimic2cdb-2.6-00/00/'+extension_1[0]+'/'
               src1 = dirname_1+'/'+'ICD9-'+extension[1]
               icd9_labels_file = 'C:/Users/Bisakha Ray/Desktop/YIN/icd9_labels_03.04.2015.txt'
               f3 = open(icd9_labels_file, 'a')
               with open(src1, 'rt') as textfile:
                   if (os.stat(src1)[6] == 0):
                       print 'icd9 file empty'
                   filetext = textfile.read()
                   matches_1 = re.findall("410.01", filetext)
                   matches_2 = re.findall("410.11", filetext)
                   matches_3 = re.findall("410.21", filetext)
                   matches_4 = re.findall("410.31", filetext)
                   matches_5 = re.findall("410.41", filetext)
                   matches_6 = re.findall("410.51", filetext)
                   matches_7 = re.findall("410.61", filetext)
                   matches_8 = re.findall("410.71", filetext)
                   matches_9 = re.findall("410.81", filetext)
                   matches_10 = re.findall("410.91", filetext)
                             
                   if matches_1 or matches_2 or matches_3 or matches_4 or matches_5 or matches_6 or matches_7 or matches_8 or matches_9 or matches_10:
                      
                      f3.write('1\n')
                   else:
                      f3.write('0\n')
               textfile.close()
               f3.close()
print count

