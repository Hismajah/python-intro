#subtract two numbers 289 and 189. you should add an if clause 
#that will check if the number is equal to 100, immediate
#divide your result by 5 and print out final result else if
#it is not equal to 100 multiply result by 6 and print out the result

a=289
b=189
f=a-b
print(f)
if f==100:
    print ("hurray it is equal to 100")
    d=f/5
    print("this is the final result",d)
else:
    print("the result is not equal to 100")
    d=f*6
    print(d)
    

