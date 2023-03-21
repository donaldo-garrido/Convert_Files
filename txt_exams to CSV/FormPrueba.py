file = open('FormPrueba.txt')
file_cont = file.readlines()

for line in file_cont:
	stripline = line.strip()
	print(stripline)
file.close()