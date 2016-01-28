Roisin Loughnane and Jeroen Hoekendijk


===========================PHYLOGENETIC TREES AND MORE===========================

The following steps are necessary manual entries before/when running the scripts:
- 'MyFolder' must be created, and also the pathway to this 'MyFolder' must be specified in ConcTree.sh (first command line in function).
- Make each script executeable in the shell using chmod command, and also source each function.
- In the ConcTree.sh script, the varibale to trim the end of the file must be typed in manually, depending on the number of input files you have (no. of input files + 4).
- In the ConcTree.sh a command called seqmagick which is not installed by default is used to convert files. To install seqmagic, complete the following steps in the shell:

1: sudo apt-get install python-pip
2: sudo pip install biopython
3: sudo pip install seqmagick

SUMMARY

This project is to construct phylogenetic trees from .fas files in a single directory (eg. MyFolder).
Additionally, one script designs primer pairs from a DNA sequence, based on the melting temperature (Tm).


TREES


The scripts for the phylogenetic tree are the following:
1. NexConc.py
2. ConcTree.sh
3. MultiTree.sh


1. NexConc.py is a python script to concatenate different .nex files to a single .nex file.
2. ConcTree.sh contains a function 'Poop' (Phylogenetic Order Of Porpoises), which produces a single phylogenetic tree from all .fas files in MyFolder. 
3. MultiTree.sh produces phylogenetic trees for each .fas file in MyFolder seperately.

DATA

There are 5 example .fas files:
ATP6_borne-Dall-Lage.fas
AT8_borne_Dall_lageno.fas
CB_borne_Dall_Lageno
COI_borne_Lage.fas
ND5_Dall.lage.fas

These were reformatted (using regular expressions) from data provided by M. Fontaine.


PRIMER DESIGN

PrimerDesign.py is a python script to design primers from a user entered sequence based on the melting temperature (Tm).
Primer length, search area, amplicon length and amplicon starting position are set as user input also.
The output shows the primer pairs that have the best matching Tm.

