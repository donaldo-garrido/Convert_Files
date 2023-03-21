import os
import csv
import docx2txt

import pdfminer
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io

contenido = os.listdir()
print(contenido)

directory = os.getcwd()
print(directory)

# replace following line with location of your .docx file


for file in contenido:
	indexExt = file.find('.')
	if indexExt >=0:
			if file[-4:] != '.csv':
				if file[-3:] != '.py':
					ext = file[file.find('.'):]
					print(ext)

					if ext == '.pdf':
						print("This is a PDF")
					elif ext == '.doc' or ext == '.docx':
						MY_TEXT = docx2txt.process(file)
						TXTname = "converted-"+file[:file.find('.')]
						with open(TXTname+".txt", "w") as text_file:
							print(MY_TEXT, file=text_file)
						text_file.close()
						file = open(TXTname+'.txt')
						file_cont = file.readlines()

						a = 'A.'
						b = 'B.'
						c = 'C.'
						d = 'D.'
						cont = 1
						preg_act = 0

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
						            choice = stripline[stripline.find(a)+3:]
						            if stripline[-2:] == '_x':
						                correctans = 'x'
						                choice = stripline[stripline.find(a)+3:-2]
						            scramble = '1'
						            question = preg
						            row_dict = {'Question':question, 'Gfb':gfb, 'Pfb':pfb, 'Ffb':ffb, 'Cfb':cfb, 'Scramble':scramble, 'Points_p_C':points_p_c, 'Choice':choice, 'Points':points, 'CorrectAns':correctans}
						            Test_writer.writerow(row_dict)


						        if stripline.find(b)>=0:
						            choice = stripline[stripline.find(b)+3:]
						            if stripline[-2:] == '_x':
						                correctans = 'x'
						                choice = stripline[stripline.find(b)+3:-2]
						            row_dict = {'Question':question, 'Gfb':gfb, 'Pfb':pfb, 'Ffb':ffb, 'Cfb':cfb, 'Scramble':scramble, 'Points_p_C':points_p_c, 'Choice':choice, 'Points':points, 'CorrectAns':correctans}
						            Test_writer.writerow(row_dict)

						        if stripline.find(c)>=0:
						            choice = stripline[stripline.find(c)+3:]
						            if stripline[-2:] == '_x':
						                correctans = 'x'
						                choice = stripline[stripline.find(c)+3:-2]
						            row_dict = {'Question':question, 'Gfb':gfb, 'Pfb':pfb, 'Ffb':ffb, 'Cfb':cfb, 'Scramble':scramble, 'Points_p_C':points_p_c, 'Choice':choice, 'Points':points, 'CorrectAns':correctans}
						            Test_writer.writerow(row_dict)

						        if stripline.find(d)>=0:
						            choice = stripline[stripline.find(d)+3:]
						            if stripline[-2:] == '_x':
						                correctans = 'x'
						                choice = stripline[stripline.find(d)+3:-2]
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

					else:
						print("No PDF or .docx")

						

with open("Output.txt", "w") as text_file:
    print(MY_TEXT, file=text_file)

def pdfparser(data):

    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    print(data)

#if __name__ == '__main__':
    #pdfparser(sys.argv[1]) 