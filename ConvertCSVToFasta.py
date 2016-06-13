csv = open("resultat.csv", 'r')
out = open("resultat.fasta", 'w')


for line in csv:
	line = line.replace('"','')
	line = line.split(",")
	out.write('>' + line[0] + '\n')
	out.write(line[1])

csv.close()
out.close()