x=input()
y=x.split()
a,b=y
s=1
while int(b)*2>=int(a)*3:
    a=int(a)*3
    b=int(b)*2
    s=s+1
print(s)    
