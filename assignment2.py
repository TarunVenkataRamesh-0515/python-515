"""
1. Write a python program to read the contents of file
and count the size of file then count how many times
“CSE” is existed in the file.
"""
import os
f1=open("Sample1.txt","r")
data=f1.read()
print("CONTENTS OF FILE: ",data)
size = os.path.getsize('Sample1.txt') #using os.path.getsize("text file name")
print('Size of file using method 1: ', size, 'bytes')
s=os.stat("Sample1.txt")#using os.stat("filename"),object.st_size
print("Size of file using method 2: ",s.st_size,"bytes")
f1.seek(0,os.SEEK_END)#by moving the cursor reading the file 
print("Size of file using method 3:",f1.tell(),"bytes")#object.tell()-->returns the size of file
occurrences=data.count("CSE")
print("Number of occurrences of CSE= ",occurrences)
f1.close()
"""
CONTENTS OF FILE:  welcome to CSE
CSE refers to computer science and engineering.this stream is the most in demand branch
Size of file using method 1:  103 bytes
Size of file using method 2:  103 bytes
Size of file using method 3: 103 bytes
Number of occurrences of CSE=  2
"""

"""
2.Develop a python code to read the contents of file and find how many upper case letters,
lower cas letters and digits are existed in the file?
text1.txt content:
HELLO WORLD I am Tarun Venkata Ramesh of CSE A bearing roll number 19A91A0515
"""
f2=open("text1.txt","r")
data=f2.read()
uc=0
lc=0
dig=0
for ch in data:
    if ch.isupper():
        uc+=1
    elif ch.islower():
        lc+= 1
    elif ch.isdigit():
        dig+=1
print("UPPER CASE LETTERS=",uc,"LOWER CASE LETTERS=",lc,"DIGITS=",dig)
f2.close()
"""
UPPER CASE LETTERS= 20 LOWER CASE LETTERS= 36 DIGITS= 8
"""

"""
3. Create a file and insert the records in the following format(Read the records from the user)
SNo      Name      Game
1	 Rahul	  Cricket
2.       David 	  Chess
3.       Ram 	  Volly Ball
"""
fp=open("GamesRecord.txt","w")
t=["SNo\t","Name\t","Game\n"]
fp.writelines(t)
n=int(input("Enter number of rows: "))
for i in range(n):
    fp.writelines([input(),"\t",input(),"\t",input()])
    fp.write("\n")
fp.close()
fp1=open("GamesRecord.txt","r")
data=fp1.read()
print(data)
fp1.close()
"""
Enter number of rows: 3
1.
Rajesh
Cricket
2.
Dinesh
Chess
3.
Ramesh
VollyBall
SNo	Name	Game
1.	Rajesh	Cricket
2.	Dinesh	Chess
3.	Ramesh	VollyBall
"""

"""
4.Consider any real time application like banking, college automation, stock market etc.,
and make use of user defined exceptions according to application and raise that exception
"""
class Age_Exception(Exception):
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))
age=int(input("Enter the age: "))
try:
    if age>=18:
        print("Eligible for voting..!!!")
    else:
        raise Age_Exception(age)
except Age_Exception as ae:
    print("Age_Exception Not eligible for voting...!!! as ",ae.value,"<18")
"""
output1:
Enter the age: 15
Age_Exception Not eligible for voting...!!! as  15 <18
output2:
Enter the age: 22
Eligible for voting..!!!
"""

