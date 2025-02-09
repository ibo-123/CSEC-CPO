x=input().split()
g=[]
s=0
for i in x:
    if i in g:
        s+=1
    else:
        g.append(i)
print(s)        