#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 22:14:29 2021

@author: xinjunzhang
"""
import os


def translate(seq):     
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein =""
    if len(seq)%3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein+= table[codon]
    return protein

translate("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

#DIR = "/Users/xinjunzhang/Desktop/QCB_Projects/Michael/"
DIR = "/u/scratch/x/xinjunzh/michael/Qseq_clean/"

all_files = os.listdir(DIR)
all_files = [f for f in all_files if "r1r2consensus.txt" in f]

for file in all_files:
    file_path = DIR+file#"BCH1_r1_clean.qseq"
    outfile_path = DIR+file[:-4]+".protein.txt"#+".target.txt"#"BCH1_r1_clean.target.txt"
    with open(file_path,"rt") as infile:
        with open(outfile_path,"wt") as outfile:
            lines = infile.readlines()
            for line in lines:
                line = line.split("\n")[0]
                if len(line)==21:
                    try:
                        protein = translate(line)
                        outfile.write(protein+"\n")
                        outfile.flush()
                    except:
                        pass
                    
                    
