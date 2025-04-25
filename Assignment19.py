"""
#Q1
x=input("Enter a string ")
for e in x:
    print(e,ord(e))


#Q2
x=input("Enter a string")
s="aeiouAEIOU"
for e in x:
    if e in s:
        print(e)
"""
#Q3
x=input("Enter a string")
c=0
for e in x:
    if e in " ":
        c+=1
print(c)

#Q5
x='34567'
c=0
for e in x:
    c+=1
print(c)

