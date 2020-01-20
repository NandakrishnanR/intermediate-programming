x=1
y=1
z=0
n=int(input("enter the limit"))
p=n-3
print("0")
print("1")
print("1")
while(p>0):
    if(p%2==0):
        z = x+ y
        x = z
    
        print(z)
    elif(p%2!=0):
        z=x+y
        y=z
    
        print(z)
    p-=1


