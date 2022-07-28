**DEMULTIPLEXING**
All work is done on talapas interactive node 
	
		srun --account=bgmp --partition=bgmp --nodes=1 --ntasks-per-node=1 --time=2:00:00 --cpus-per-task=1 --pty bash

create bash variable to link to file directory, I did this in my sbatch script
	Datafiles directory
		dir="/projects/bgmp/shared/2017_sequencing"
	All other files
		/projects/bgmp/ano/Bi622/Demultiplex/Assignment-the-first

**Assignment the First***
 intial file exploration, turn in answers.md file
 
	 zcat 1294_S1_L008_R1_001.fastq.gz | wc -l

question iii. count all the reads with a N read aka unknown reads
	zcat 1294_S1_L008_R1_001.fastq.gz | sed -n '2~4p' | grep -c N

Unit Tests
Wrote unit tests for sequences each with a different output.
Expected outputs
	2 matched
	2 hopped
	2 unknown

expout_r1_AA.fastq
expout_r2_AA.fastq
expout_r1_hopped.fastq
expout_r2_hopped.fastq
expout_r1_unknown.fastq


**Bio622 ASSIGNMENT THE FIRST PSEUDO CODE**
**Goal**: We need to parse through 4 seperate line matched files and sort them in to the proper subfiles by barcode. Index files need to be assessed and determine whether they match, are hopped or unmatched. The corresponding lines from the read files need to be stored according to the determination made by analyzing the index files. Also, our files are very very large so we want to loop through these files as few times as possible.

**Output**: All output files will be fastQ files
1 output file for each matched index(24) for each read direction(2) = 1*24*2 = 48 

1 output file for hopped forward reads and reverse reads = 2

1 output file for unmatched reads (contain N) for each direction = 2

    52 total output files


**Pseudocode**
$with open -> Read in input files
$import -> Import modules

 Simultaneously run through both Read files (R1, R4) and both Index files (R2, R3)

    At every sequence line check for:

        IF -> If the barcodes from R2 match the REVERSE compliment barcode of R3 

            AND -> the Q_score is higher than DEFINED CUTOFF

                AND -> the index files contain no 'N's

                    THEN -> STORE the record from the same lines in R1/R4 in "<MatchedR#>.fq"

        
        ELSEIF -> the barcodes from R2 do NOT match the R3 reverse compliment 
                AND -> do not contain a 'N'
                    AND -> are above Q-score CUTOFF
                    THEN -> store record in "<hoppedR#>.fq"

            ELSE -> STORE in "unmatchedR#.fq"

    At every Q-score line CONVERT_PHRED the qscores and check each position to see if it is below our assigned QSCORE CUTOFF then STORE in "unmatchedR#.fq"

**note**
create variables in loop to compare index1 vs. reverse compliment of index1 like..
I1_seq = filehand2.readline[c]
I2_seq = filehand3.readline[c]
    I2_seq = REVERSE_COMPLIMENT_FUNCTION[I2]

**High Level Functions and Commands**
WITH OPEN
IMPORT
IF ELSE
ELSEIF
AND

CONVERT_PHRED
    inputs quality scores[str] converts in to phred scores [in]
        returns phred per base pair

REVERSE_COMPLIMENT_FUNCTION
    inputs a sequence converts to the reverse compliment and stores in variable
        then compares to a sequence in a different file at the same line
            returns whether there is a match, hopped, or unmatched