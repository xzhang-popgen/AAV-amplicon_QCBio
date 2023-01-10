# AAV-amplicon_QCBio
Scripts and files for computing the enrichment of AAV amplicon (project personnel involved: Prof. Melissa Spencer and Dr. Michael Enami at UCLA)


For each sample, we keep the sequenced reads from the demultiplexed Qseq files where the primer sequences are present and precisely matched. The sequencing was performed as pair-ended, and we keep only the target sequences if the forward and backward reads are consistent. Variants of 21 bps length enclosed by the primer sequences are further extracted, and are translated into peptide sequences of 7 amino acids length. We compute the abundance of variants by counting the number of all unique variants in a given sample, and we further normalize the abundance by the sequencing reads of the sample. The enrichment score (E) of each variant is computed as the ratio between the normalized abundance in P2 sample versus P1 sample. 
