import os
import csv

nameYN = input('¿Los contenidos se llamarán como los archivos?, responda SI o NO: ')
if nameYN == 'SI':
	name = 1
else:
	name = 0

scormYN = input('¿Hay Paquetes SCORM?, responda SI o NO: ')
if scormYN == 'SI':
	scorm = 1
else:
	scorm = 0

dominio = input('Dominio al que pertenece el contenido:')

folder = input('Escriba el folder o ruta del folder en que se depositará el contenido, recuerde que se usa \\ para viajar entre folders: ')
print(folder)

contenido = os.listdir()
print(contenido)

directory = os.getcwd()
print(directory)

count = 0
template = 'Standard Content Player Template'
server = 'Default Saba Content Server'
vendor = 'Saba'

with open('BulkContentImport.csv', mode='w') as BCI:
	fieldnames = ['ID', 'CONTENTTITLE', 'CONTENTFORMAT', 'SPLIT', 'PLAYERTEMPLATE', 'CONTENTFOLDER', 'CONTENTSERVER', 'DELIVERYVENDOR', 'ZIPFILENAME']

	BCI_writer = csv.DictWriter(BCI, fieldnames=fieldnames,quotechar = '"')
	BCI_writer.writeheader()
	for file in contenido:
		original_file_name = file

		file = file.replace('á','a')
		file = file.replace('é','e')
		file = file.replace('í','i')
		file = file.replace('ó','o')
		file = file.replace('ú','u')
		file = file.replace('Á','A')
		file = file.replace('É','E')
		file = file.replace('Í','I')
		file = file.replace('Ó','O')
		file = file.replace('Ú','U')

		print(file)
		
		os.rename(directory+'/'+original_file_name,directory+'/'+file)
		indexExt = file.find('.')
		if indexExt >=0:
			if file[-4:] != '.csv':
				if file[-3:] != '.py':
					ext = file[file.find('.'):]
					print(ext)
					count += 1
					iD = str(count)
					if ext == '.pdf':
						Cformat = 'Archivo'
					elif ext == '.doc' or ext == '.docx':
						Cformat = 'Archivo'
					elif ext == '.xls' or ext == '.xlsx':
						Cformat = 'Archivo'
					elif ext == '.zip':
						Cformat = 'Archivo zip'
					else:
						Cformat = ' '

					if name == 1:
						title = file[:indexExt]
					else:
						title = input('Título del contenido No.'+file[:2]+': ')
					row_dict = {'ID':iD, 'CONTENTTITLE':title, 'CONTENTFORMAT':Cformat, 'SPLIT':dominio, 'PLAYERTEMPLATE':template, 'CONTENTFOLDER':folder, 'CONTENTSERVER':server, 'DELIVERYVENDOR':vendor, 'ZIPFILENAME':file}
					BCI_writer.writerow(row_dict)

