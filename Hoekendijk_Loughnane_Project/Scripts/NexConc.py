#! /usr/bin/env python
#
# Roisin Loughnane and Jeroen Hoekendijk
#
# The combine function takes a list of tuples [(name, nexus instance)...], 
# if we provide the file names in a list we can use a list comprehension to 
# create these tuples
#
# SOURCE:
# biopython.org/wiki/Concatenate_nexus


################################ IMPORT MODULES ################################

import os
import sys


################################ SCRIPT ########################################

FileList = os.popen('ls *.nex').read().split()

from Bio.Nexus import Nexus

nexi = [(fname, Nexus.Nexus(fname)) for fname in FileList]

combined = Nexus.combine(nexi)
combined.write_nexus_data(filename=open('CombinedSeq.nex', 'w'))

print # creates blank line
print 'Combined Nexus file created :-)'
print # creates blank line
