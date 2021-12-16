import pandas as pd
import numpy as np
from csv import reader
import csv
import datetime
import sys
import shutil
import os
import time
import smtplib, ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import numpy as np
import openpyxl
import xlrd
import os
from email.mime.base import MIMEBase
from email import encoders
import xlsxwriter 
import shutil
#import pywintypes
from win10toast import ToastNotifier
import xlwt
from xlwt import Workbook
import shutil
import string
from datetime import datetime
df=' '
count=0
flag2=0
mail=0
#print('vaibhav')
while 1:
	#t=0
	#Flag=0
	#while 1:
		#t+=1
	try:
		Flag=0
		#shutil.os.remove('C:/Excel/Excel_diff.txt')
		#t=0
		#try:
		while 1:
		
			#t+=1
			#print('vaibhav')
			APP_FOLDER = 'C:/Users/3011313/Desktop/ICT_Project/Reference_Files'
			totalFiles = 0
			for base, dirs, files in os.walk(APP_FOLDER):
    				#print('Searching in : ',base)
    				for Files in files:
        				totalFiles += 1
			#print('Total number of files',totalFiles)
			path="C:/Users/3011313/Desktop/ICT_Project/Log_Files"
			os.chdir(path)
			files=sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
			oldest=files[0]
			newest=files[-1]
			#count=count+1
			if oldest.startswith('W'):
				first_chars = oldest[0:9]
				first_chars2=first_chars+'.CSV'
				#print(first_chars2)
			else:
				if oldest.startswith('w'):
					first_chars = oldest[0:10]
					first_chars2=first_chars+'.CSV'
					#print(first_chars2)
				else:
					pathD="C:/Users/3011313/Desktop/ICT_Project/Log_Files/"
					os.chdir(pathD)
					filesD=sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
					oldestD=files[0]
					newestD=files[-1]
					shutil.os.remove(pathD+oldestD)
					break
					#sliced = oldest[2:]
					#print(sliced)
					#first_chars, rest = sliced.split('_', 1)
					#first_chars2=first_chars+'.CSV'
					#print(first_chars2)
			#program = pd.read_csv(newest, nrows=1)
			Lcols=['DEVICE','REFER.','LIMIT-','(-%)','LIMIT+','(+%)']
			Lcols2=['DEVICE'] 
			A = pd.read_csv (oldest,usecols=Lcols,header=3,skipinitialspace=True)
			C = pd.read_csv (oldest,usecols=Lcols2,header=3,skipinitialspace=True) 
			A.to_csv('C:/Users/3011313/Desktop/ICT_Project/Files/Log10.csv',index=False,header=True)
			C.to_csv('C:/Users/3011313/Desktop/ICT_Project/Files/Log2.csv',index=False,header=True)
			t10 = open('C:/Users/3011313/Desktop/ICT_Project/Files/Log10.csv','r')
			outFile10 = open('C:/Users/3011313/Desktop/ICT_Project/Files/Log.csv', 'w')
			for row in t10:
				for cell in row:
					outFile10.write(cell.strip())
				outFile10.write("\n")
			t1 = open('C:/Users/3011313/Desktop/ICT_Project/Files/Log.csv','r')
			t3 = open('C:/Users/3011313/Desktop/ICT_Project/Files/Log2.csv','r')
			#shutil.move(oldest ,'C:/Users/3011313/Desktop/ICT_Project/Reference_Files/abc.csv')
			path2="C:/Users/3011313/Desktop/ICT_Project/Reference_Files"
			os.chdir(path2)
			files2=sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
			oldest2=files[0]
			newest2=files[-1]
			#print('1')
			#print(files2)
			for x in range(totalFiles):
				#print(files2[x])
				#print(files2[x])
				if first_chars2==files2[x]:
					print(first_chars2)
					print(files2[x])
					#df=pd.read_csv(newest, skiprows=1)
					#print('2')
					B = pd.read_csv (files2[x],usecols=Lcols,header=3)
					#print('3')
					#pathM="C:/Users/3011313/Desktop/ICT_Project/Master/"
					#print('4')
					D = pd.read_csv (files2[x],usecols=Lcols2,header=3)
					#print('5')
					B.to_csv('C:/Users/3011313/Desktop/ICT_Project/Files/Ref20.csv',index=False,header=True)
					t20 = open('C:/Users/3011313/Desktop/ICT_Project/Files/Ref20.csv','r')
					outFile20 = open('C:/Users/3011313/Desktop/ICT_Project/Files/Ref.csv', 'w')
					for row in t20:
						for cell in row:
							outFile20.write(cell.strip())
						outFile20.write("\n")
					D.to_csv('C:/Users/3011313/Desktop/ICT_Project/Files/Ref2.csv',index=False,header=True)
					t2 = open('C:/Users/3011313/Desktop/ICT_Project/Files/Ref.csv', 'r')
					t4 = open('C:/Users/3011313/Desktop/ICT_Project/Files/Ref2.csv', 'r')
					#if flag2==0:
						#flag2=1
						#shutil.move(files2[x],'C:/Users/3011313/Desktop/ICT_Project/Master')
					#else:
					#shutil.os.remove(files2[x])
					#os.rename('C:/Users/3011313/Desktop/ICT_Project/Reference_Files/abc.csv',files2[x])
					#shutil.copy(fileone2 ,'C:/Users/3011313/Desktop/ICT_Project/Reference_Files/abc.csv')
					fileone = t1.readlines()
					filetwo = t2.readlines()
					filethree = t3.readlines()
					filefour = t4.readlines()
					t1.close()
					t2.close()
					t3.close()
					t4.close()
					outFile = open('C:/Users/3011313/Desktop/ICT_Project/Files/out.txt', 'a')
					outFile2 = open('C:/Users/3011313/Desktop/ICT_Project/Files/out.csv', 'a')
					outFile3 = open('C:/Users/3011313/Desktop/ICT_Project/Files/change.csv', 'a')
					outFile4 = open('C:/Users/3011313/Desktop/ICT_Project/Files/delete.csv', 'a')
					td = open('C:/Users/3011313/Desktop/ICT_Project/Files/delete.csv', 'r')
					ts = open('C:/Users/3011313/Desktop/ICT_Project/Files/change.csv', 'r')
					files = ts.readlines()
					ts.close()
					filed = td.readlines()
					td.close()
					writer = csv.writer(outFile)
					#writer.writerow(["DATE", "TIME", "DEVICE","LIMIT-","LIMIT+"])
					#writer.writerow([datetime.datetime.now(),outFile])
					#print('6')
					if oldest!=df:
						y = 0
						x = 0
						k = 0
						j = 0
						m = 0
						#i = 0
						for j in filefour:
							remove = string.whitespace
							if filethree[m].strip() == filefour[y].strip():
								#print(m)
								#print(filethree[m].strip())
								for i in fileone:
									if fileone[k].strip() != filetwo[x].strip():
										s=0
										s2=1
										flags=0
										for s in files:
											#print(fileone[s2])
											if s==fileone[k]:
												#print(s)
												#print(fileone[s2])
												flags=1
										if flags==0:
											#print('11')
											path="C:/Users/3011313/Desktop/ICT_Project/Log_Files"
											os.chdir(path)
											files=sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
											oldest=files[0]
											newest=files[-1]
											with open(oldest) as oldest_file:
												data = csv.reader(oldest_file)
												for row in list(data)[0:2]:
								 					writer.writerow([row])
													#oldest_file.close() 
											#writer.writerow(["DATE              --->    ",datetime.datetime.now()]) 
											writer.writerow(["Refrence File     --->    ",filetwo[x] ])
											writer.writerow(["Log File          --->    ",fileone[k] ])
											outFile3.write(fileone[k])
											writer.writerow(["---------------------------------------------------------------------------------------------"])
											mail=1
											df=oldest
											Flag=1
											path_log="C:/Users/3011313/Desktop/ICT_Project/Log_Files/"
											#shutil.os.remove(path_log+oldest)
											outFile2.write(filethree[m])
											#print(oldest)
											#print(fileone[k])
											#print(filetwo[x])
											#print(filethree[m])
											x+=1
											k+=1
										
									else:
										x+=1
										k+=1
									break
								y+=1
								m+=1
							else:
								outFile4 = open('C:/Users/3011313/Desktop/ICT_Project/Files/delete.csv', 'a')
								td = open('C:/Users/3011313/Desktop/ICT_Project/Files/delete.csv', 'r')
								filed = td.readlines()
								td.close()
								s=0
								flagd=0
								for s in filed:
									if s==filefour[y]:
										flagd=1
								if flagd==0:
									path_log="C:/Users/3011313/Desktop/ICT_Project/Log_Files/"
									os.chdir(path_log)
									files=sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
									oldest=files[0]
									newest=files[-1]
									with open(oldest) as oldest_file:
										data = csv.reader(oldest_file)
										for row in list(data)[0:2]:
											writer.writerow([row])
									writer.writerow(["This Device is DeletedR         --->    ", filefour[y]])
									#writer.writerow(["This Device is DeletedL         --->    ", filefour[m]])
									outFile4.write(filefour[y])
									writer.writerow(["---------------------------------------------------------------------------------------------"])
									mail=1
									#print(filefour[y])
								df=oldest
								y+=1
								x+=1
								#m+=1
								Flag=1
								#td.close()
								#k+=2
					path_log="C:/Users/3011313/Desktop/ICT_Project/Log_Files/"
					os.chdir(path_log)
					files=sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
					oldest=files[0]
					newest=files[-1]
					shutil.os.remove(path_log+oldest)
					#shutil.move(path_log+oldest,'C:/Users/3011313/Desktop/ICT_Project/Backup')
					#outFile.close()
					#ts.close()
					#td.close()
					#time.sleep(1)
								#count=count+1	
		
	
		
													 
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")
			if (current_time>='06:15:00' and current_time<='06:17:30')or(current_time>='14:15:00' and current_time<='14:17:30')or(current_time>='22:15:00' and current_time<='22:17:30'):
				if mail==1:
					mail=0
					path="C:/Users/3011313/Desktop/ICT_Project/Files//"
					with open(path+"out.txt") as f:
						with open(path+"out2.txt", "w") as f1:
							for line in f:
								f1.write(line)
					fromaddr = "vaibhav_aher1313@jabil.com"
					toaddr = "sopan_aher@jabil.com"
					toaddr2 = "vaibhav_aher1313@jabil.com"
					toaddr3 = "VENKATESWARLU_PATIBANDLA@jabil.com"
					toaddr4 = "prashant_shinde9300@jabil.com"
					toaddr5 = "Abasaheb_Tambe@Jabil.com"
					toaddr6 = "Pradip_Nagmode4@jabil.com"
					#instance of MIMEMultipart
					msg = MIMEMultipart()
					#storing the senders email address  
					msg['From'] = fromaddr
					#storing the receivers email address 
					msg['To'] = toaddr2
					#storing the subject
					msg['Subject'] = "Changes in Limits"
					#string to store the body of the mail
					#body = """\
					#Hello Sir,
					#Subject: Changes in limits
					#Following limits has changed."""
					with open(path+'out2.txt','r') as file:
						countriesStr=file.read()
					#t2 = open('C:/Users/3011313/Desktop/ICT_Project/Files/Excel_diff.txt', 'r')
					#fileon = t1.readlines()
					# attach the body with the msg instance
					msg.attach(MIMEText(countriesStr, 'plain'))
					#open the file to be sent 
					filename =  path+'out2.txt'
					attachment = open(path+'out2.txt', "rb")
					#instance of MIMEBase and named as p
					p = MIMEBase('application', 'octet-stream')
					# To change the payload into encoded form
					p.set_payload((attachment).read())
					# encode into base64
					encoders.encode_base64(p)
					p.add_header('Content-Disposition', "attachment;filename= %s" % filename)
					# attach the instance 'p' to instance 'msg'
					msg.attach(p)
					# creates SMTP session
					s = smtplib.SMTP('smtp.office365.com', 587)
					# start TLS for security
					s.starttls()
					# Authentication
					s.login(fromaddr, "MNBVCXZ@123")
					# Converts the Multipart msg into a string
					text = msg.as_string()
					# sending the mail
					#s.sendmail(fromaddr, toaddr, text)
					s.sendmail(fromaddr, toaddr2, text)
					#s.sendmail(fromaddr, toaddr3, text)
					#s.sendmail(fromaddr, toaddr4, text)
					#s.sendmail(fromaddr, toaddr5, text)
					#s.sendmail(fromaddr, toaddr6, text)
					# terminating the session
					s.quit()
					print('Mail Sent')
					#mail=0
					ff=df
					time.sleep(200)
					outFile3.close()
					outFile4.close()
					outFile.close()
					shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/out.txt')
					#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/Ref.csv')
					#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/Ref2.csv')
					#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/Log.csv')
					#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/Log2.csv')
					#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/out.csv')
					shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/change.csv')
					shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/delete.csv')
				
					#path="C:/Users/3011313/Desktop/ICT_Project/Reference_Files"
					#os.chdir(path)
					#files=sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
					#oldest=files[0]
					#newest=files[-1]
					#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Reference_Files/UDP.csv')
					#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Reference_Files/UDV.csv')
					#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Reference_Files/GXY.csv')
					#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Reference_Files/W1125601.csv')
					#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Reference_Files/W1119919.csv')
					#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Reference_Files/W1110372.csv')



					#path="C:/Users/3011313/Desktop/ICT_Project/Master"
					#os.chdir(path)
					#files=sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
					#oldest=files[0]
					#newest=files[-1]
					#shutil.copy('C:/Users/3011313/Desktop/ICT_Project/Master/UDP.csv' , 'C:/Users/3011313/Desktop/ICT_Project/Reference_Files')
					#shutil.copy('C:/Users/3011313/Desktop/ICT_Project/Master/UDV.csv' , 'C:/Users/3011313/Desktop/ICT_Project/Reference_Files')
					#shutil.copy('C:/Users/3011313/Desktop/ICT_Project/Master/GXY.csv' , 'C:/Users/3011313/Desktop/ICT_Project/Reference_Files')
					#shutil.copy('C:/Users/3011313/Desktop/ICT_Project/Master/W1125601.csv' , 'C:/Users/3011313/Desktop/ICT_Project/Reference_Files')
					#shutil.copy('C:/Users/3011313/Desktop/ICT_Project/Master/W1119919.csv' , 'C:/Users/3011313/Desktop/ICT_Project/Reference_Files')
					#shutil.copy('C:/Users/3011313/Desktop/ICT_Project/Master/W1110372.csv' , 'C:/Users/3011313/Desktop/ICT_Project/Reference_Files')
					#flag2=0
				
				
		





	except:
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		if (current_time>='06:15:00' and current_time<='06:17:30')or(current_time>='14:15:00' and current_time<='14:17:30')or(current_time>='22:15:00' and current_time<='22:17:30'):
			if mail==1:
				mail=0
				path="C:/Users/3011313/Desktop/ICT_Project/Files//"
				with open(path+"out.txt") as f:
					with open(path+"out2.txt", "w") as f1:
						for line in f:
							f1.write(line)
				fromaddr = "vaibhav_aher1313@jabil.com"
				toaddr = "sopan_aher@jabil.com"
				toaddr2 = "vaibhav_aher1313@jabil.com"
				toaddr3 = "VENKATESWARLU_PATIBANDLA@jabil.com"
				toaddr4 = "prashant_shinde9300@jabil.com"
				toaddr5 = "Abasaheb_Tambe@Jabil.com"
				toaddr6 = "Pradip_Nagmode4@jabil.com"
				#instance of MIMEMultipart
				msg = MIMEMultipart()
				#storing the senders email address  
				msg['From'] = fromaddr
				#storing the receivers email address 
				msg['To'] = toaddr2
				#storing the subject
				msg['Subject'] = "Changes in Limits"
				#string to store the body of the mail
				#body = """\
				#Hello Sir,
				#Subject: Changes in limits
				#Following limits has changed."""
				with open(path+'out2.txt','r') as file:
					countriesStr=file.read()
				#t2 = open('C:/Users/3011313/Desktop/ICT_Project/Files/Excel_diff.txt', 'r')
				#fileon = t1.readlines()
				# attach the body with the msg instance
				msg.attach(MIMEText(countriesStr, 'plain'))
				#open the file to be sent 
				filename =  path+'out2.txt'
				attachment = open(path+'out2.txt', "rb")
				#instance of MIMEBase and named as p
				p = MIMEBase('application', 'octet-stream')
				# To change the payload into encoded form
				p.set_payload((attachment).read())
				# encode into base64
				encoders.encode_base64(p)
				p.add_header('Content-Disposition', "attachment;filename= %s" % filename)
				# attach the instance 'p' to instance 'msg'
				msg.attach(p)
				# creates SMTP session
				s = smtplib.SMTP('smtp.office365.com', 587)
				# start TLS for security
				s.starttls()
				# Authentication
				s.login(fromaddr, "mnbvcxz@123")
				# Converts the Multipart msg into a string
				text = msg.as_string()
				# sending the mail
				#s.sendmail(fromaddr, toaddr, text)
				s.sendmail(fromaddr, toaddr2, text)
				#s.sendmail(fromaddr, toaddr3, text)
				#s.sendmail(fromaddr, toaddr4, text)
				#s.sendmail(fromaddr, toaddr5, text)
				#s.sendmail(fromaddr, toaddr6, text)
				# terminating the session
				s.quit()
				print('Mail Sent')
				#mail=0
				ff=df
				time.sleep(200)
				outFile.close()
				outFile3.close()
				outFile4.close()
				shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/out.txt')
				#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/Ref.csv')
				#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/Ref2.csv')
				#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/Log.csv')
				#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/Log2.csv')
				#shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/out.csv')
				shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/change.csv')
				shutil.os.remove('C:/Users/3011313/Desktop/ICT_Project/Files/delete.csv')

						