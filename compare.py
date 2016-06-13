csv = open("resultat.csv", 'r')
sequence = "MKRNILAVIVPALLIAGTANAAEIYNKDGNKVDLYGKAVGLHYFSKGNGENSYGGNGDMTYARLGFKGETQINSDLTGYGQWEYNFQGNNSE"
print len(sequence)
nb = 0


for line in csv:
	line = line.replace('"','')
	line = line.split(",")
	if sequence in line[1]  :
		nb += 1

print nb

