#! /usr/bin/env python
# Roisin Loughnane and Jeroen Hoekendijk


###################### NOTES ######################
#
# Example values:
# Put in a sequence of 150-200 Bp
# Primer Length: 12
# SearchArea: 17
# AmpliconLength: 35
# AmpliconStart: 50

# The Search Area is the area in which primers are grabbed.
# The AmpliconLength is the length of the target fragment to amplify
# AmpliconStart is the position where the target fragment to amplify starts


###################### IMPORT MODULES ######################

import math

###################### GET VARIABLES ######################

# Define a DNA sequence in the terminal, change to capitals and remove spaces
print # Create blank line
print '==============PRIMER DESIGN==============' # some visual aid
print 'by Roisin Loughnane and Jeroen Hoekendijk'
print # Create blank line
DNASeq = raw_input('Enter a DNA sequence: ')
DNASeq = DNASeq.upper()
Seq = DNASeq.replace(" ","")

# ERROR check 1:
# Determine if there are invalid  characters (e.g. other than ACGT):
for i in range(0, len(Seq)):
	if Seq[i] != 'A' and Seq[i] != 'T' and Seq[i] != 'C' and Seq[i] != 'G':
		print 'ERROR: You have entered an unknown symbol', Seq[i],'in position ', i, '.'
		print 'The program will now exit.'
		exit() # Exit program

# Some output text about the entered sequence
print # Create blank line
print 'You have entered the following DNA sequence (gaps removed, all capitals):'
print Seq # Prints the sequence
print 'Length of DNA sequence =', len(Seq), 'Bp' # Prints the length of the sequence
print # Create blank line

# Define the primer length, the search area, the length of the amplicon... 
# ...and the starting position of the amplicon in the terminal
PrimerL = int(raw_input('Enter the length of the primer: '))
SearchArea = int(raw_input('Enter the search area: '))
AmpliconL = int(raw_input('Enter the length of the amplicon: '))
AmpliconStart = int(raw_input('Enter the starting position of the amplicon: '))
print # Create blank line

# ERROR check 2:
# Check if SearchArea doesn't exceed the number of available Bp's (e.g. AmpliconStart)
if SearchArea > AmpliconStart:
	print 'ERROR: Your search area exceeds the number of Bp available (e.g. AmpliconStart)'
	print 'You have entered:'
	print 'Search area:', SearchArea, 'Bp'
	print 'The amplicon starts in position:', AmpliconStart
	print 'Search area will be adjusted to the maximum possible Bps'
	SearchArea = AmpliconStart
	print 'New search area:', SearchArea, 'Bp'

# ERROR check 3:
# Check if the primer length doesn't exceed the the search area
if PrimerL > SearchArea:
	print 'ERROR: Your primer length exceeds the search area'
	print 'You have entered:'
	print 'Primer length:', PrimerL, 'Bp'
	print 'Search area:', SearchArea, 'Bp'
	print 'The program will now exit.'
	print # Create blank line
	exit() # Exit program

# Print variables to screen
print '======================================' # some visual aid
print # Create blank line
print 'SUMMARY:'
print 'Primer length:', PrimerL, 'Bp'
print 'Search area:', SearchArea, 'Bp'
print 'Length of the amplicon:', AmpliconL, 'Bp'
print 'The amplicon starts in position:', AmpliconStart
print # Create blank line
print '======================================' # some visual aid
print # Create blank line

# More error checks should be made for the end of the sequence and the reverse primers.



###################### FORWARD PRIMERS ######################

# Define empty string
FwdPrimers=[]

# Get forward primers from Seq
# -1 is to compensate for starting point is strings
for i in range(AmpliconStart-SearchArea, AmpliconStart-PrimerL):
	FwdPrimers.append(Seq[i:i+PrimerL])
print 'All possible FwdPrimers within search area:'
print FwdPrimers
print # Create blank line


###################### REVERSE PRIMERS ######################

# Define empty string
RevPrimers=[]

# Get reverse primers from Seq
# -1 is to compensate for starting point is strings
for i in range(AmpliconStart+AmpliconL, AmpliconStart+AmpliconL+SearchArea-PrimerL):
	RevPrimers.append(Seq[i:i+PrimerL])

# Define empty string for mirrored reverse primers
RevPrimers2=[[0 for x in range(PrimerL)] for y in range(len(RevPrimers))]

# Get mirrored reverse primers from RevPrimers
for i in range(0, len(RevPrimers)):
	for j in range(0, PrimerL):
		if RevPrimers[i][j] == 'A':
			RevPrimers2[i][j] = 'T'
		elif RevPrimers[i][j] == 'T':
			RevPrimers2[i][j] = 'A'
		elif RevPrimers[i][j] == 'C':
			RevPrimers2[i][j] = 'G'
		elif RevPrimers[i][j] == 'G':
			RevPrimers2[i][j] = 'C'

# put the individual bases of the primers back in one string per primer,
# for display and easy usage
for i in range(0, len(RevPrimers2)):
	RevPrimers2[i]= ''.join(RevPrimers2[i])


print 'All possible RevPrimers within search area:'
print RevPrimers2
print # Create blank line
print '======================================' # some visual aid
print # Create blank line



###################### MELTING TEMPERATURE ######################

# Define empty list for FwdPrimers + Tm		
FwdPrimersTm=[[0 for x in range(PrimerL +1)] for y in range(len(FwdPrimers))]
# Fill FwdPrimers + Tm list
for i in range(0, len(FwdPrimers)):
	for j in range(0, PrimerL +1):
		if j == PrimerL:
			TotalStrong = FwdPrimers[i].count('C') +FwdPrimers[i].count('G') # define number of C's and G's
			TotalWeak = FwdPrimers[i].count('A') +FwdPrimers[i].count('T') # define number of A's and T's
			if PrimerL >= 14: # if length of sequence is 14 or greater, continue
				# formula for sequences that are 14 or more nucleotides long
				FwdPrimersTm[i][j] = 64.9 + 41 * (TotalStrong - 16.4) / PrimerL
			else: # if lengt of sequence is smaller than 14
				# formula for sequences that are less than 14 nucleotides long:
				FwdPrimersTm[i][j] = (4 * TotalStrong) + (2 * TotalWeak) # formula to calculate melting temperature
		else:
			FwdPrimersTm[i][j] = FwdPrimers[i][j] # add fwd primer sequence
			

# Define empty list for RevPrimers + Tm		
RevPrimersTm=[[0 for x in range(PrimerL +1)] for y in range(len(RevPrimers2))]
# Fill RevPrimers + Tm list
for i in range(0, len(RevPrimers2)):
	for j in range(0, PrimerL +1):
		if j == PrimerL:
			TotalStrong = RevPrimers2[i].count('C') +RevPrimers2[i].count('G') # define number of C's and G's
			TotalWeak = RevPrimers2[i].count('A') +RevPrimers2[i].count('T') # define number of A's and T's
			if PrimerL >= 14: # if length of sequence is 14 or greater, continue
				# formula for sequences that are 14 or more nucleotides long
				RevPrimersTm[i][j] = 64.9 + 41 * (TotalStrong - 16.4) / PrimerL
			else: # if lengt of sequence is smaller than 14
				# formula for sequences that are less than 14 nucleotides long
				RevPrimersTm[i][j] = (4 * TotalStrong) + (2 * TotalWeak) # formula to calculate melting temperature
		else:
			RevPrimersTm[i][j] = RevPrimers2[i][j] # add RevPrimer sequences

# Define empty string with Difference (Delta) Tm and primer codons
DeltaTm=[[0 for x in range(3)] for y in range(len(FwdPrimers)*len(RevPrimers2))]

# Fill Delta Tm + primer codon list
for i in range(0, len(FwdPrimers)):
	for j in range(0, len(RevPrimers2)):
		x = math.fabs(RevPrimersTm[i][PrimerL]-FwdPrimersTm[j][PrimerL]) # returns absolute values
		DeltaTm[(i*len(FwdPrimers))+j][0] = x # returns Tm
		DeltaTm[(i*len(FwdPrimers))+j][1] = FwdPrimers[i] # returns fwd primer codon
		DeltaTm[(i*len(FwdPrimers))+j][2] = RevPrimers2[j] # returns rev primer codon

# Create sorted DeltaTm
DeltaTmSorted=sorted(DeltaTm)

# Define the number of pairs to display
NumberOfPairs = 10

# Print results
print # Create blank line
print '=============BEST PRIMERS============='
print 'Ranked by melting temperature (Tm)'
for i in range(0, NumberOfPairs):
	print i+1, DeltaTmSorted[i]


