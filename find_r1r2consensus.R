setwd("~/Desktop/QCB_Projects/Michael/")

setwd("/u/scratch/x/xinjunzh/michael/Qseq_clean/")

all_files <- list.files(pattern = "clean.withinfo.txt")

names <- c()
for (i in 1:length(all_files)){
  names <- c(names,unlist(strsplit(all_files[i],"_"))[1])
}
names <- unique(names)

library(dplyr)

for (name in names){
  r1 <- read.table(paste0(name,"_r1_clean.withinfo.txt"),stringsAsFactors = F,sep = "\t")
  r2 <- read.table(paste0(name,"_r1_clean.withinfo.txt"),stringsAsFactors = F,sep = "\t")
  
  r1 <- left_join(r1,r2,by="V1")
  r1 <- r1[complete.cases(r1),]
  
  consensus <- r1[(r1$V2.x==r1$V2.y),]
  
  consensus <- consensus[nchar(consensus$V2.x)==21,]
  
  write.table(consensus$V2.x,sep = "\n",file=paste0(name,".r1r2consensus.txt"),quote = F,row.names = F,col.names = F)
  print(name)
  r1 = c()
  r2=c()
}

