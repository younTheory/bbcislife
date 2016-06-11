from Bio.Align.Applications import MuscleCommandline
from Bio import AlignIO

muscle_loc = r'/home/aurel/Documents/HEIG-VD/Semestre6/BBC/muscle'

in_file = 'resultat.fasta'
out_file = 'e_coli.aln'

muscle_cline = MuscleCommandline(cmd=muscle_loc,input=in_file,out=out_file,clwstrict=True)
stdout, stderr = muscle_cline()

muscle_align = AlignIO.read(out_file,'clustal')
print(muscle_align)
