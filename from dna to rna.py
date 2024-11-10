from Bio.Seq import Seq

coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")


template_dna = coding_dna.reverse_complement()


messenger_rna = coding_dna.transcribe()


print("Coding DNA:", coding_dna)
print("Template DNA (Reverse Complement):", template_dna)
print("Messenger RNA:", messenger_rna)
