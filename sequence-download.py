from Bio import Entrez
import time
Entrez.email = "prenom.nom@heig-vd.ch"


query = '"ompf"[gene] AND "Escherichia coli"[porgn]'
handle = Entrez.esearch(db='nucleotide',retmax=5,term=query)
record = Entrez.read(handle)
gi = record['IdList']

csv = open('resultat.csv', 'w')
csv.write('sep=,\n')
csv.write("\"" + "Protein_ID" + "\",\"" + "Translation" + "\"\n")

start = time.clock()
for i in gi:
  protein_info = Entrez.efetch(db="nucleotide",id=i,rettype="gb",retmode="xml")
  protein_info = Entrez.read(protein_info)
  table_features = protein_info[0]['GBSeq_feature-table']

  for j in table_features :
	  features = j['GBFeature_quals']

	  ompf = 0
	  translation = ""
	  prot = ""
	  for f in features:
		if f['GBQualifier_name'] == 'gene' and f['GBQualifier_value'].lower() == "ompf":
			ompf = 1
		if f['GBQualifier_name'] == 'translation':
			translation = f['GBQualifier_value']
		if f['GBQualifier_name'] == "protein_id" :
			prot = f['GBQualifier_value']
		if translation and prot and ompf:
			csv.write("\"" + prot + "\",\"" + translation + "\"\n")
			break
		
print "time taken", time.clock() - start, "seconds"
csv.close()