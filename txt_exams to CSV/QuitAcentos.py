import csv

csvList = []
archivo = input('Nombre del CSV: ')
with open(archivo) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
    	rowStr = row[0]
    	
    	rowStr = rowStr.replace('Ã¡','a')
    	rowStr = rowStr.replace('Ã©','e')
    	rowStr = rowStr.replace('Ã³','o')
    	rowStr = rowStr.replace('Ã­','i')
    	rowStr = rowStr.replace('Ã±','ñ')
    	
    	csvList.append(rowStr)


with open('result_file.csv', mode='w') as result_file:
    result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for line in csvList:
    	result_writer.writerow([line])