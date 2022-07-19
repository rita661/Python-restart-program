for x in range(1,6): #(1-6)
    print(x)
    
for x in range(1,50):#print hi 50 times
    print('hi')
    
#calculate square number btw 2 to 10
for x in range(2,11):
    print(x*x)
    
#checking for even numbers
if x%2==0:
    print(x)
    
#checking for odd numbers
if x%2!=0:
    print(x)
#if else statement
if x%2==0:
    print("even number:", x)
else:
    print("odd number:",x)
    
L1=[10,20, 70,60,30,40,50]
print (L1)

for x in L1:
    print(x)
print(len(L1))
print(max(L1))
print(min(L1))

#SUM OF ALL NUMBERS IN LIST
sum=0
for x in L1:
    sum=sum+x
    print(sum)

