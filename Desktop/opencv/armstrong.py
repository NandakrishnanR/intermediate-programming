x=input("enter a number to  be checked")
summ=0
temp=x
l=len(x)
while l>0:
 digit = int(temp) % 10
 summ += digit ** 3
 int(temp)//10
 l=l-1
if temp == x :
    print("the number{0} is armstrong".format(x))
else:
    print("not armstrong") 
    
