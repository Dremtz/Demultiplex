#!/usr/bin/env python

#run these in bash before script
#1. $srun --account=bgmp --partition=bgmp --nodes=1 --ntasks-per-node=1 --time=2:00:00 --cpus-per-task=1 --pty bash
#2. $dir="/projects/bgmp/shared/2017_sequencing"

import numpy as np
import bioinfo
import matplotlib.pyplot as plt
import gzip
import argparse

def get_args():
    parser = argparse.ArgumentParser(description = "client input program")
    parser.add_argument("-f", "--filename", help = "specify filename", type=str, required = True)
    parser.add_argument("-r", "--readlength", help = "specify readlength", type=int, required = True)
    parser.add_argument("-o", help = "specify outfile name", type=str, required = True)

    return parser.parse_args()

#make arg input name easier to type
clinput = get_args()
f = clinput.filename
r = clinput.readlength
o = clinput.o


#create a numpy array that we will fill with mean values
fa_array = np.zeros(r,dtype=np.int64) #should the end length by length of file? (wc -l)/4?

numrecord = 0
with gzip.open(f,"rt") as fh: #open file
        i = 0
        
        for line in fh: #iterate through input file
            i+=1
            line = line.strip('\n') #strip new line characters
            
            if i%4 == 0: #grab every 4th line (q score line)
                numrecord = int(i/4) -1
                if numrecord % 100000 == 0 : 
                    print(f"Current Record Is {numrecord}")
                for c,s in enumerate(line): #populates list using c for counter and s for conver_phred. Lets us do two different calculations at the same spot
                    score = bioinfo.convert_phred(s) 
                    # fa_array[c,l] = score
                    fa_array[c] += score
                        
#create empty array and call it 'mean'
mean = np.zeros(r, dtype=float)

#populate array w/ np.mean function
# for i in range(r):
#     mean[i] = fa_array[i]/numrecord

# another way of coding the above
mean = fa_array/numrecord
   
    
#np.mean(fa_array[i])

plt.bar(range(r), mean)
plt.xlabel("Sequence Postition")
plt.ylabel("Mean Quality Score")
plt.title("Mean Quality Scores by Position for FastQ File")
plt.savefig(o+'.png')