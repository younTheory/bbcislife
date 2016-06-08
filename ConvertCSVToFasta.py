#!/usr/local/bin/python

#docstring= """
#DESCRIPTION
#    Convert tabular to FASTA

#USAGE:
#    python tab2fasta.py <tab-file> <sequence column> <header column 1> <header column 2> <header column n>  > <outfile>
#

#import sys
#if len(sys.argv) < 4:
#    sys.exit('\nThree or more arguments required%s' %(docstring))
    
csv = open("resultat.csv", 'r')
out = open("resultat.fasta", 'w')
#seqix= int(sys.argv[2]) - 1 
#headerix= sys.argv[3:]
#headerix= [(int(x) - 1) for x in headerix]

for line in csv:
	line = line.replace('"','')
	line = line.split(",")
	out.write('>' + line[0] + '\n')
	out.write(line[1])

csv.close()
out.close()