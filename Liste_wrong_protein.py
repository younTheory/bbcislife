csv = open("resultat.csv", 'r')
out = open("wrong.txt", 'w')

for line in csv:
	line = line.replace('"','')
	line = line.split(",")
	if len(line[1]) < 100 :
		print line[0] 


csv.close()
out.close()
