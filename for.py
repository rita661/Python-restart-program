#for loop- initialization, condition, increment/decrement
x=5
while x<11:
    print(x)
    x=x+1
print()

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    
    myMixedTypeList2 = ["jack is my favourite name.", 23,1.67,False,23.9]
    for element in myMixedTypeList2:
        print("{} is of the data type {}".format(element,type(element)))
