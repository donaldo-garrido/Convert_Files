import csv
with open('Test2140.csv', mode='w') as Test:
    Test_writer = csv.writer(Test, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    Test_writer.writerow(['No_Reactivo','Reactivo','Opción A)','Opción B)','Opción C)','Opción D)'])

    Test_writer.writerow(['John Smith', 'Accounting', 'November'])
    Test_writer.writerow(['Erica Meyers', 'IT', 'March'])