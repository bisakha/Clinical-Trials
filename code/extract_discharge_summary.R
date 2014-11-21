for (filename in list.files("C:/Users/Bisakha Ray/Desktop/YIN/NoteEvents_filtered/")){
inputfile = paste("C:/Users/Bisakha Ray/Desktop/YIN/NoteEvents_filtered/",filename,sep="")
print(inputfile)
dat <- read.csv(inputfile,header=TRUE)
mylist <- dat[dat$CATEGORY=="DISCHARGE_SUMMARY",]
outfile = paste("C:/Users/Bisakha Ray/Desktop/YIN/DischargeSummaries_filtered/",filename,sep="")
writeLines(unlist(lapply(mylist, paste, collapse=" ")), con = outfile)}
