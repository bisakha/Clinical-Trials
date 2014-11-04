for (filename in list.files("C:/Users/Bisakha Ray/Desktop/YIN/NoteEvents/")){
inputfile = paste("C:/Users/Bisakha Ray/Desktop/YIN/NoteEvents/",filename,sep="")
print(inputfile)
dat <- read.csv(inputfile,header=TRUE)
dat[dat$CATEGORY=="DISCHARGE_SUMMARY",]
outfile = paste("C:/Users/Bisakha Ray/Desktop/YIN/DischargeSummaries/",filename,sep="")
writeLines(unlist(lapply(mylist, paste, collapse=" ")), con = outfile)}
