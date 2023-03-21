import csv

file = open('FormPrueba.txt')
file_cont = file.readlines()
a = ' a) '
b = ' b) '
c = ' c) '
d = ' d) '
cont = 1
preg_act = 0

with open('Test2140.csv', mode='w') as Test:
    Test_writer = csv.writer(Test, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    Test_writer.writerow(['No_Reactivo','Reactivo','Opción A)','Opción B)','Opción C)','Opción D)'])
    for line in file_cont:
    	stripline = line.strip()
    	#print(stripline[0:2])
    	#print(stripline)
    	#print(preg_act)
    	if stripline.find(a)>0:
    		a_p = stripline[stripline.find(a)+3:]
    	if stripline.find(b)>0:
    		b_p = stripline[stripline.find(b)+3:]
    	if stripline.find(c)>0:
    		c_p = stripline[stripline.find(c)+3:]
    	if stripline.find(d)>0:
    		d_p = stripline[stripline.find(d)+3:]
    		Test_writer.writerow([num,preg,a_p,b_p,c_p,d_p])
    	if preg_act == 1:
    		num = str(cont)
#    		Test_writer.writerow(corr_ans)
    		preg = stripline
    		#Test_writer.writerow([num,preg,a_p,b_p,c_p,d_p])
    		preg_act = 0
    		cont = cont+1
    	if stripline[0:3] == str(cont)+'.':
    		preg_act = 1
    	
file.close()