#python code to add numbers together
list1=[2,5,6,7,8,3,4,2,3,1]
#print (sum())
total=0
for y in list1:
    total=total+y
print(total)
#check if total is greater than 50, if yes, divide by 20 and add 19. otherwise add 500
if total>50:
    print("Hurray total is greater than 50")
    result=(total/20)+19
    print(result)
else:
    result=total+500
    print(result)