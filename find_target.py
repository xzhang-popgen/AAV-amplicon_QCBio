#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 20:44:33 2022

@author: xinjunzhang
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:31:04 2021

@author: xinjunzhang
"""
import os 
import numpy as np
import pandas as pd
import argparse
import re
import gzip


upstream = "tggacaagtggccacaaaccaccagagtggccaagcaggc"
upstream = upstream.upper()
downstream = "gcccaggcggccaccggctgggttcaaaaccaaggaatac"
downstream = downstream.upper()
#reverse_upstream = upstream[::-1]
#reverse_downstream = downstream[::-1]

target = "TGTAATTGTCCGGCGTTGAAT" 
#reverse_target = "ACATTAACAGGCCGCAACTTA"

complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
#seq = "TCGGGCCC"
#reverse_complement = "".join(complement.get(base, base) for base in reversed(seq))


#DIR = "/Users/xinjunzhang/Desktop/QCB_Projects/Michael/"
DIR = "/u/scratch/x/xinjunzh/michael/Qseq_clean/"

all_files = os.listdir(DIR)
all_files = [f for f in all_files if "qseq" in f]

for file in all_files:
    file_path = DIR+file#"BCH1_r1_clean.qseq"
    outfile_path = DIR+file[:-5]+".withinfo.txt"#+".target.txt"#"BCH1_r1_clean.target.txt"
    find = ""
    count = 0
    count_find = 0
    count_findr = 0
    with open(file_path,"rt") as infile:
        with open(outfile_path,"wt") as outfile:
            lines = infile.readlines()
            for line in lines:
                fields = line.split("\t")
                line = fields[8]
                info = fields[3]+"-"+fields[4]
                result = re.search(upstream+'(.*)'+downstream, line)
                #line_reverse = line[::-1]
                line_reverse = "".join(complement.get(base, base) for base in reversed(line))
                result_reverse = re.search(upstream+'(.*)'+downstream, line_reverse)
                count+=1
                try:
                    find = find+result.group(1)
                    outfile.write(info+"\t"+find+"\n")
                    find = ""
                    count_find+=1
                except:
                    try:
                        find = find+result_reverse.group(1)
                        outfile.write(info+"\t"+find+"\n")
                        find = ""
                        count_findr+=1
                    except:
                        pass
                #if len(find)>0
    print(file)
    print(count)
    print(count_find)
    print(count_findr)
    

#s = upstream+target+downstream
#result = re.search(upstream+'(.*)'+downstream, s)
#print(result.group(1))
