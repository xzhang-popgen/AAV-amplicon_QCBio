setwd("~/Desktop/QCB_Projects/Michael/protein/")

##crreate a function that computes enrichment
compute_enrichment <- function(comp,sample_name){
  all_var <- unique(comp)
  count_comp <- c()
  for (v in all_var){
    count_comp <- c(count_comp,sum(comp==v))
  }
  
  #max(count_comp)
  #hist(count_comp)
  
  rank_comp <- data.frame(all_var,count_comp)
  colnames(rank_comp) <- c("sequence",sample_name)
  return(rank_comp)
}
##

##compute enrichment
read_depth <- read.csv("read_depth.csv",stringsAsFactors = F)

comp1 <- readLines("BCD1.r1r2consensus.protein.txt") #56
comp2 <- readLines("BCF10.r1r2consensus.protein.txt") #78

rank_comp1 <- compute_enrichment(comp1,"56")
rank_comp2 <- compute_enrichment(comp2,"78")

colnames(rank_comp1)[2] <- paste0("X",56)
colnames(rank_comp2)[2] <- paste0("X",78)

write.table(rank_comp1,"enrichment_sample56.txt",row.names = F,quote = F,sep = "\t")
write.table(rank_comp2,"enrichment_sample78.txt",row.names = F,quote = F,sep = "\t")

##normalize enrichment, get ratio
#automated, specify P2 and P1
P2=56
P1=78

rank_comp1 <- read.delim(paste0("enrichment_sample",P2,".txt"),stringsAsFactors = F)
rank_comp2 <- read.delim(paste0("enrichment_sample",P1,".txt"),stringsAsFactors = F)

library(dplyr)
comp_set1 <- full_join(rank_comp1,rank_comp2,by="sequence")

colnames(comp_set1)[2:3] <- c("P2","P1")

comp_set1$normalize_P2 <- comp_set1$P2/read_depth$depth[read_depth$ID==P2]
comp_set1$normalize_P1 <- comp_set1$P1/read_depth$depth[read_depth$ID==P1]

comp_set1_sort <- comp_set1[order(-comp_set1$normalize_P2),]

comp_set1_sort$E = comp_set1_sort[,4]/comp_set1_sort[,5]

write.csv(comp_set1_sort,paste0("comp_",P2,"-",P1,"_sort.csv"),row.names = F)

library(ggplot2)
ggplot(comp_set1_sort, aes(x = E)) + geom_histogram() + scale_x_log10()+ ggtitle(paste0("P2=",P2,", P1=",P1))+theme(plot.title = element_text(hjust = 0.5))

