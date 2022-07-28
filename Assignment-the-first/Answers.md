# Assignment the First

## Part 1
1. Be sure to upload your Python script.

| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz |bio1  |101  | 33 |
| 1294_S1_L008_R2_001.fastq.gz |index1  |8  | 33 |
| 1294_S1_L008_R3_001.fastq.gz |index2  |8  | 33 |
| 1294_S1_L008_R4_001.fastq.gz |bio2  |101  | 33 |

2. Per-base NT distribution
    1. Use markdown to insert your 4 histograms here.

![](https://github.com/Dremtz/Demultiplex/blob/master/Assignment-the-first/R1_Histogram_a1.png)
![](https://github.com/Dremtz/Demultiplex/blob/master/Assignment-the-first/R2_A1_graph.png)
![](https://github.com/Dremtz/Demultiplex/blob/master/Assignment-the-first/R3_A1_graph.png)
![](https://github.com/Dremtz/Demultiplex/blob/master/Assignment-the-first/R4_Histogram_a1.png)
    2. **Cutting off at 35 seems like an appropriate data cutoff since the quality score for the early sequences degrades fairly sharply from the upper ~39 to <36 in sequence positions under 10. Also, trimming at Qscore 35 will retain the majority of our data**
    3. **Index2 = 3976613, Index3 = 3328051
 zcat 1294_S1_L008_R2_001.fastq.gz | sed -n '2~4p' | grep -c N**
    
## Part 2
1. Define the problem
**We need to parse through 4 seperate line matched files and sort them in to the proper subfiles by barcode. Index files need to be assessed and determine whether they match, are hopped or unmatched. The corresponding lines from the read files need to be stored according to the determination made by analyzing the index files. Also, our files are very very large so we want to loop through these files as few times as possible.**
2. Describe output

**All output files will be fastQ files
1 output file for each matched index(24) for each read direction(2) = 1*24*2 = 48 
1 output file for hopped forward reads and reverse reads = 2
1 output file for unmatched reads (contain N) for each direction = 2
    52 total output files**

3. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).
4. Pseudocode
5. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement
