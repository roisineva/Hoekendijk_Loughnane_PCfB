#! /bin/bash
#
# Roisin Loughnane and Jeroen Hoekendijk

# This script firstly uses a for loop to run through .fas files in a folder (eg. MyFolder) created prior to running the script and for each .fas file sequences are aligned using clustalw.
# The output files for the for loop are in .nex format. A python script then concatenates these files into a single .nex file.
# The end of this file must be trimmed using the head command (!!!! manual entry here as number of lines vary depending on number of input files !!!!!)
# Seqmagick (which must be manually installed prior to running this script) then converts this file back to .phy in order to be create the phylogenetic tree.
# Source: http://www.biopython.org/wiki/Concatenate_nexus

#START:

POOP(){
	# Set directory where fasta folders are located
	cd ~/Porpoise_Data/mtDNA/MyFolder/ # This could be improved, and set as user input

	FILES=*.fas # Grab .fas files
	BOOTS=10
	OutFile=Tree_Fig # Set name for outfile

	for f in $FILES # Process through .fas files
	do
		clustalw -infile=$f -type=DNA -outfile=$f.nex -output=NEXUS # Align the sequences using clustal-w and produce .nex file
	done

	# Concatenate different Nexus files
	NexConc.py

	head -n -9 CombinedSeq.nex > CombinedSeq2.nex #!!! Manually change -9 here if number of .fas files differ

	seqmagick convert --output-format phylip --alphabet dna CombinedSeq2.nex CombinedSeq2.phy # Converts back to .phy

	phyml -i CombinedSeq2.phy -d nt -n 1 -b $BOOTS -m HKY85 # Run phyml to estimate the best phylogenetic tree
	nw_display -s -S -v 25 -b ’opacity:0’ -i ’font-size:8’     CombinedSeq2.phy_phyml_tree.txt > $OutFile.svg # Created tree image

}
