import csv
import os

contenido = os.listdir()
print(contenido)
for txtFile in contenido:
    indexExt = txtFile.find('.')
    if indexExt >=0:
        if txtFile[-4:] != '.csv':
            if txtFile[-3:] != '.py':
                ext = txtFile[-4:]
                #TXTname =  input('Ingrese el nombre del archivo de texto sin la extensión .txt:')
                TXTname = txtFile[:-4]
                file = open(TXTname+'.txt')
                file_cont = file.readlines()

                a = 'A. a.'
                b = 'B. b.'
                c = 'C. c.'
                d = 'D. d.'
                cont = 1
                preg_act = 1

                with open(TXTname+'.csv', mode='w') as Test:
                    fieldnames = ['Question', 'Gfb', 'Pfb', 'Ffb', 'Cfb', 'Scramble', 'Points_p_C', 'Choice', 'Points', 'CorrectAns']

                    Test_writer = csv.DictWriter(Test, fieldnames=fieldnames,quotechar = '"')
                    Test_writer.writeheader()
                    for line in file_cont:
                        stripl = line.replace(';',',')
                        stripline = stripl.strip()

                        question = ''
                        gfb = ''
                        pfb = ''
                        ffb = ''
                        cfb = ''
                        scramble = ''
                        points_p_c = ''
                        choice = ''
                        points = ''
                        correctans = ''

                        row_dict = {'Question':question, 'Gfb':gfb, 'Pfb':pfb, 'Ffb':ffb, 'Cfb':cfb, 'Scramble':scramble, 'Points_p_C':points_p_c, 'Choice':choice, 'Points':points, 'CorrectAns':correctans}

                        if stripline.find(a)>=0:
                            choice = stripline[stripline.find(a)+5:]
                            if stripline[-2:] == '_x':
                                correctans = 'X'
                                choice = stripline[stripline.find(a)+5:-2]
                            scramble = ''
                            question = preg
                            row_dict = {'Question':question, 'Gfb':gfb, 'Pfb':pfb, 'Ffb':ffb, 'Cfb':cfb, 'Scramble':scramble, 'Points_p_C':points_p_c, 'Choice':choice, 'Points':points, 'CorrectAns':correctans}
                            Test_writer.writerow(row_dict)


                        if stripline.find(b)>=0:
                            choice = stripline[stripline.find(b)+5:]
                            if stripline[-2:] == '_x':
                                correctans = 'X'
                                choice = stripline[stripline.find(b)+5:-2]
                            row_dict = {'Question':question, 'Gfb':gfb, 'Pfb':pfb, 'Ffb':ffb, 'Cfb':cfb, 'Scramble':scramble, 'Points_p_C':points_p_c, 'Choice':choice, 'Points':points, 'CorrectAns':correctans}
                            Test_writer.writerow(row_dict)

                        if stripline.find(c)>=0:
                            choice = stripline[stripline.find(c)+5:]
                            if stripline[-2:] == '_x':
                                correctans = 'X'
                                choice = stripline[stripline.find(c)+5:-2]
                            row_dict = {'Question':question, 'Gfb':gfb, 'Pfb':pfb, 'Ffb':ffb, 'Cfb':cfb, 'Scramble':scramble, 'Points_p_C':points_p_c, 'Choice':choice, 'Points':points, 'CorrectAns':correctans}
                            Test_writer.writerow(row_dict)

                        if stripline.find(d)>=0:
                            choice = stripline[stripline.find(d)+5:]
                            if stripline[-2:] == '_x':
                                correctans = 'X'
                                choice = stripline[stripline.find(d)+5:-2]
                            row_dict = {'Question':question, 'Gfb':gfb, 'Pfb':pfb, 'Ffb':ffb, 'Cfb':cfb, 'Scramble':scramble, 'Points_p_C':points_p_c, 'Choice':choice, 'Points':points, 'CorrectAns':correctans}
                            Test_writer.writerow(row_dict)
                        if preg_act == 1:
                            num = str(cont)
                            preg = stripline
                            preg_act = 0
                            cont = cont+1
                        if stripline == str(cont)+'.':
                            preg_act = 1

                file.close()
