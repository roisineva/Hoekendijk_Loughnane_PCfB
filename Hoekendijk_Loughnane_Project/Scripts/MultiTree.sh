#! /bin/bash
#
# Roisin Loughnane and Jeroen Hoekendijk
#

# Before running this script, a folder with the .fas files needs to be created:
# The first folder (here called: "~/Porpoise_Data/mtDNA/MyFolder") needs to contain your target .fas files.

# The folder containing the ouput files (here called: "~/Porpoise_Data/mtDNA/OutputFolder/") is created during the script using mkdir command.



 # Set directory where fasta files are located
cd ~/Porpoise_Data/mtDNA/MyFolder/ # This could be improved, and set as user input
mkdir ~/Porpoise_Data/mtDNA/OutputFolder/ # Creates folder for output files


FILES=*.fas # Grab .fas files

for f in $FILES # Process through .fas files
do
  echo $f # Prints filename
  echo "$f contains the following sequences:" # Prints filename and text to screen
  grep ">" $f # Grabs the sequences, defined in the .fas file with ">"
  echo "Total number of sequences:" # Displays text on screen
  grep -c ">" $f # Counts sequences

  mkdir ~/Porpoise_Data/mtDNA/OutputFolder/$f # Make new directory 'folder2' for output
  cp ./$f ~/Porpoise_Data/mtDNA/OutputFolder/$f # Copy fasta file to this new folder
  cd ~/Porpoise_Data/mtDNA/OutputFolder/$f # Change directory to this new folder

  BOOTS=10 # Set Bootstrap value
  clustalw -infile=$f -type=DNA -outfile=out_ali.phy -output=PHYLIP # Align the sequences using clustal-w 
  phyml -i out_ali.phy -d nt -n 1 -b $BOOTS -m HKY85 # Run phyml to estimate the best phylogenetic tree

  OutFile=Tree_Fig # Set name for outfile

  # Display the tree using the nw_display utility
  nw_display -s -S -v 25 -b ’opacity:0’ -i ’font-size:8’ 	out_ali.phy_phyml_tree.txt > $OutFile.svg

  cd ~/Porpoise_Data/mtDNA/MyFolder/ # Change back to directory containing .fas files
done # End of for loop
