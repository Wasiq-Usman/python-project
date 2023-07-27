import random
n = int(input("Enter no of elements you want in your list: "))
l=[]
num = int(input("Enter num to specify range: "))
for i in range (1,n+1,1):
    num = random.randint(0,num)
    l.append(num)
print("Random numbers list:", l)
input ("Enter any key to exit")
