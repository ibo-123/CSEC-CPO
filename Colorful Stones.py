x=input()
y=input()
h=[]
l=[]
h.extend(x)    
l.extend(y)
s=0
m=1
for i in l:
    if i==h[s]:
        m+=1
        s+=1
print(m)            
        