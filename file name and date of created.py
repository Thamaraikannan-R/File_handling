import os, sys
import os.path, time
org={'1.txt','2.txt', '3.txt', '4.txt', '5.txt', '6.txt'}
path = "C:\\Users\\lotus\\Desktop\\new"
filename = os.listdir( path )
filename=set(filename)
not_present=set(org.symmetric_difference(filename))
filename=org.intersection(filename)
if(len(not_present)>0):
	print("These files are not available.")
	for i in not_present:
		print("--> ",i)
else:
	print("All files present")
print("These are available files with name and date of created:")
print("Name_of_file\tTime of created")
filename=list(filename)
filename.sort()
for file in filename:
	print(file,"\t\t\t",end='')
	s=''
	s=path
	s=s.__add__('\\')
	s=s.__add__(file)
	print(time.ctime(os.path.getmtime(s)))