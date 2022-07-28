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
![]()
![]()
![]()
    2. **Cutting off at 35 seems like an appropriate data cutoff since the quality score for the early sequences degrades fairly sharply from the upper ~39 to <36 in sequence positions under 10. Also, trimming at Qscore 35 will retain the majority of our data**
    3. **Index2 = 3976613, Index3 = 3328051
 zcat 1294_S1_L008_R2_001.fastq.gz | sed -n '2~4p' | grep -c N**
    
## Part 2
1. Define the problem
2. Describe output
3. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).
4. Pseudocode
5. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement
