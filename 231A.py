
import string
x= input()
z=0
for var in range(int(x)) :
    y=input()
    t = int(y[0])+ int(y[2])+int(y[4])
    if t>1:
        z+=1
print(z)