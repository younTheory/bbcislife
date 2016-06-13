from Bio.Blast.Applications import NcbiblastpCommandline
query = 'NNAGFLDSNLIIVLNDN'  
blastp_cline = NcbiblastpCommandline(db="nr", outfmt=5) 
out, err = blastp_cline(stdin=query)
print out
print err