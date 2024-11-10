from bio import seqI0

max_sequence_id = None
max_gc_content = 0
for seq_record in seqI0.parse("gc_content.fast", "fasta"):
    
   sequence = str(seq_record.seq)
   sequence_id = seq_record.id
   gc_content = (sequence.count("c") + sequence.count("G")) /len(sequence) * 100
   if gc_content > max_gc_content :
       max_sequence_id = sequence_id
       max_gc_content = gc_content
       
       print (max_sequence_id)
       print (max_gc_content)
   