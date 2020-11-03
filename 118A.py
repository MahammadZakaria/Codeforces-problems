import string
x= input()
y=''
vowel = ['a','u','e','y','o','i','I','A','U','E','Y','O']
for var in range(len(x)):
    if x[var] in vowel :
      y=y
    else:
        y+='.'+x[var]
print(y.lower())