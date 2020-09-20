f = open('rosalind_dna.txt')
s = f.read()
print (str(s.count('A')) + " " + str(s.count('C')) + " " + str(s.count('G')) + " " + str(s.count('T')))