x=input()
y=[]
y.extend(x)
s=0
g=0
for i in y:
    c=i
    if i == c.lower():
        s+=1
    else:
        g+=1
if s>g:
    print(x.lower())            
elif g>s:
    print(x.upper())  
else:
    print(x.lower())      