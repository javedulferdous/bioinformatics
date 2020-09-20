f = open('rosalind_rna.txt')
s = f.read()
rna = s.replace('T','U')
print ('RNA:', rna)