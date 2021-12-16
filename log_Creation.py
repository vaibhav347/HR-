import mysql.connector as c
import csv
import os
import shutil
Duplicate_File = 'C:/Users/3011313/Desktop/Prashant/Short/out2.txt'  #This is extra file to avoid duplicate failures
path="C:/Users/3011313/Desktop/Prashant/Files/"                      #Detailed file path
os.chdir(path)
files=sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
oldest=files[0]                                              #oldest file in detailed path folder
newest=files[-1]                                             #newest file in detailed path folder
print(path+newest)
print(newest)
outFile = open('C:/Users/3011313/Desktop/Prashant/Short/'+newest, 'a')     #short file create
outFile2 = open(Duplicate_File, 'w')                                      

#Detailed ICT file scan

string1 = '@BATCH'
file1 = open(path+newest, "r")
for line in file1:  
	if string1 in line:
		print(line)
		outFile.write(line.strip())
		outFile.write('\n')
		break
string1 = '@BTEST'
#file1 = open("C:/Users/3011313/Desktop/Prashant/210916001428INRJNM0NCRICT081_n4003512137N00188_PASS.log", "r")
for line in file1:  
	if string1 in line:
		print(line)
		outFile.write(line.strip())
		outFile.write('\n')
		break 
string1 = '@CUST'
#file1 = open("C:/Users/3011313/Desktop/Prashant/210916001428INRJNM0NCRICT081_n4003512137N00188_PASS.log", "r")
for line in file1:  
	if string1 in line:
		print(line)
		outFile.write(line.strip())
		outFile.write('\n')
		break 
string1 = '@Division'
#file1 = open("C:/Users/3011313/Desktop/Prashant/210916001428INRJNM0NCRICT081_n4003512137N00188_PASS.log", "r")
for line in file1:  
	if string1 in line:
		print(line)
		outFile.write(line.strip())
		outFile.write('\n')
		break 
string1 = '@BSTYLE'
#file1 = open("C:/Users/3011313/Desktop/Prashant/210916001428INRJNM0NCRICT081_n4003512137N00188_PASS.log", "r")
for line in file1:  
	if string1 in line:
		print(line)
		outFile.write(line.strip())
		outFile.write('\n')
		break 
string1 = '@SITE'
#file1 = open("C:/Users/3011313/Desktop/Prashant/210916001428INRJNM0NCRICT081_n4003512137N00188_PASS.log", "r")
for line in file1:  
	if string1 in line:
		print(line)
		outFile.write(line.strip())
		outFile.write('\n')
		break 
string1 = '@LINE'
#file1 = open("C:/Users/3011313/Desktop/Prashant/210916001428INRJNM0NCRICT081_n4003512137N00188_PASS.log", "r")
for line in file1:  
	if string1 in line:
		print(line)
		outFile.write(line.strip())
		outFile.write('\n')
		#outFile.write("}")
		#outFile.write("}")
		break 

#code for pass files

fileS = open(path+newest, "r")
stringS = '@BTEST'
stringSS = '|00|'
#lineS=0
flagg=0
for lineS in fileS:
	if (stringS in lineS)and(stringSS in lineS):
		print(lineS)
		outFile.write("}")
		outFile.write('\n')
		outFile.write("}")
		flagg=1
		break;

fileS = open(path+newest, "r")
stringS = '@BTEST'
stringSS = '|14|'
#lineS=0
flagg=0
for lineS in fileS:
	if (stringS in lineS)and(stringSS in lineS):
		print(lineS)
		flagg=2
		break;

#code for jet files
if flagg == 2:
			flag_pin = 0
			pin1 = '{@RPT|TestJet Report for "testjet".}'
			pin2 = '{@RPT|----------------------------------------}'
			pin3 = '{@RPT|Shorts Report for "shorts".}'
			lines = file1.readlines()
			for lineP in reversed(lines):
				if pin2 in lineP:
					flag_pin=1
				if flag_pin == 1:
					outFile2.write(lineP.strip())
					outFile2.write('\n')
				if (pin1 in lineP)or(pin3 in lineP):
					break
			outFile2.close()
			outFile3 = open(Duplicate_File, 'r')
			lines = outFile3.readlines()
			for lineP in reversed(lines):
				outFile.write(lineP.strip())
				outFile.write('\n')
			outFile.write("}")
			outFile.write('\n')
			outFile.write("}")
			outFile3.close()
		
if flagg == 0:  #code for failure data
	
			fileF = open(path+newest, "r")
			file_search = open(path+newest, "r")
			stringF = 'HAS FAILED'
			stringFF = '{@RPT|----------------------------------------}'
			flag = 0
			index = 0
			flag_search=0
			file_path = path+newest
			file_text = open(file_path, "r")
			a=True
			while a:
				file_line = file_text.readline()
				if not file_line:
					a = False
				for lineF in fileF:  
					if stringF in lineF:
						resF = lineF[:-13]
						resFF = resF[6:]
						resFFF='{@BLOCK|'+resFF+'|00'
						flag_search=0
						file_search = open(path+newest, "r")
						for search in file_search:
							if resFFF in search:
								print(resFFF)
								flag_search=1
								break
						file_search.close()
						if flag_search == 0:
							outFile2 = open(Duplicate_File, 'r+')
							flagR=0
							for row in outFile2:
								if row == lineF:
									flagR=1
									outFile2.close()
									break
							if flagR == 0: 
								#outFile2.close()
								outFile.write(lineF.strip())
								outFile.write('\n')
								outFile2.write(lineF.strip())
								outFile2.write('\n')
								outFile2.close()
								for lineF in fileF:
									outFile.write(lineF.strip())
									outFile.write('\n')
									if stringFF in lineF:
										break
			#code for pins and short
			fileF.close()
			file_search.close()
			file_text.close()
			flag_pin = 0
			pin1 = '{@RPT|CHEK-POINT Report for "pins".}'
			pin2 = '{@RPT|------End,'
			pin3 = '{@RPT|Shorts Report for "shorts".}'
			lines = file1.readlines()
			for lineP in reversed(lines):
				if pin2 in lineP:
					flag_pin=1
				if flag_pin == 1:
					outFile2.write(lineP.strip())
					outFile2.write('\n')
				if (pin1 in lineP)or(pin3 in lineP):
					break
			outFile2.close()
			outFile3 = open(Duplicate_File, 'r')
			lines = outFile3.readlines()
			for lineP in reversed(lines):
				outFile.write(lineP.strip())
				outFile.write('\n')
			outFile.write("}")
			outFile.write('\n')
			outFile.write("}")
			outFile3.close()
	
		
file1.close()
outFile.close()
fileS.close()
#os.remove('C:/Users/3011313/Desktop/Prashant/Short/pins.txt')
shutil.move(path+newest,'C:/Users/3011313/Desktop/Prashant/Backup/')    #move detailed file in backup folder
