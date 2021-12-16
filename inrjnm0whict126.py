import shutil
import glob,os
path2 ="C:/Users/3011313/Desktop/ICT_Project/Log_Files"
os.chdir("//inrjnm0whict126/c$/DATA")
#os.chdir("//inrjnm0whict5m2/c$/DATA")
#os.chdir("//inrjnm0whict5m1/c$/DATA")
#os.chdir("//inrjnm0whict01/c$/DATA")
while 1:
	for file in glob.glob("**.csv", recursive = True):
		try:
			shutil.copy(file,path2)
			print(file)
		#except FileNotFoundError:
		except:
        		print("Wrong file or file path")
			
				
	


