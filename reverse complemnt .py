from Bio.Seq import seq

dna_string = Seq("GTCAACGCTTCCGACA")


reverse_complement_dna = dna_string.reverse_complement()


print("DNA string:", dna_string)
print("Reverse complement:", reverse_complement_dna)