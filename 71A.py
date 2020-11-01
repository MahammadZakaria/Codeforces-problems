y= int(input())
i=int(1)
s=""
x=""
 
while i<=y:
          x= str(input())
          if len(x) > 10 :
              s += x[0] + str(len(x) - 2) + x[len(x) - 1] + "\n"
          else:
                s+=str(x)+"\n"
 
          i+=1
 
 
print(s)