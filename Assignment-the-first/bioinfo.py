#DEMUX PART1 COPY
# Author: <Andreas Martinez> <ano@uoregon.edu>
# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - 
#https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module
'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
You should update this docstring to reflect what you would like it to say'''
__version__ = "0.1"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning


DNAbases = set('ATGCNatcgn')
RNAbases = set('AUGCNaucgn')

    ###CONVERT_PHRED###
def convert_phred(letter: str) -> int:
    """Converts a single character into a phred score"""
    return ord(letter) -33


    ########QUAL_SCORE#############
def qual_score(phred_score: str) -> float:
    """Write your own doc string"""
    
    y = len(phred_score)
    x = 0

    for values in phred_score:
        
        total=convert_phred(values)
        
        x += total
   
    return(x/y)


    #########GC CONTENT##########
def gc_content(DNA):
    '''Returns GC content of a DNA sequence as a decimal between 0 and 1.'''
    DNA = DNA.upper()         #Make sure sequence is all uppercase
    Gs = DNA.count("G")       #count the number of Gs
    Cs = DNA.count("C")       #count the number of Cs
    return (Gs+Cs)/len(DNA)
    pass

    
def oneline_fasta():
    '''docstring'''
    pass
#if __name__ == "__main__":
    # write tests for functions above