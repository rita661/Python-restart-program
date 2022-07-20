import re
insulin ='''ORIGIN
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//'''
newstring = re.sub(r'[0-9]+','', insulin)#remove numbers
newstring1 = re.sub(r'\s', '', newstring)#removed spaces
str3=newstring1.replace('//','') #removed //
str4 = re.sub(r'[A-Z]', '', str3) #removed ORIGIN
print(str4)

#print(newstring)

#insulin1=re.sub(r'[\s0-9//A-Z]', '', insulin)
#print(insulin1)

#calling the length function
print(len(str4))
print()

#lsinsulin-seq-clean.txt
file1=open("/home/ec2-user/environment/week1.py/preproinsulin-seq-clean.txt", "r")


filels=open("/home/ec2-user/environment/week1.py/lsinsulin-seq-clean.txt","w")
data=file1.read(24)
filels.write(data)
print(data)


fileA=open("/home/ec2-user/environment/week1.py/binsulin-seq-clean.txt","w")
data=file1.read(30)
fileA.write(data)
print(data)


fileB=open("/home/ec2-user/environment/week1.py/cinsulin-seq-clean.txt","w")
data=file1.read(35)
fileB.write(data)
print(data)


fileC=open("/home/ec2-user/environment/week1.py/ainsulin-seq-clean.txt","w")
data=file1.read(21)
fileC.write(data)
print(data)





file1.close()
fileA.close()
fileB.close()
fileC.close()
filels.close()




