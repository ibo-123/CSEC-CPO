x=input()
y='abcdefghijklmnopqrstuvwxyz'
l=[]
l.extend(x)
h=[]
h.extend(y)
s=0
a='a'
for i in l:
    d=h.index(a)
    b=h.index(i)
    if d<=b:
        j=y[d:b]
    else:
        j=y[b:d]    
    if len(j)<=13:
        s+=len(j)
    elif len(j)>13:
        s+=26-len(j)
    a=i      
print(s)    
    