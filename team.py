x=int(input())
z=[]
m=0
for i in range(x):
    y=input().split()
    z.append(y)
for i in z:
    c=i.count("1")
    if c>1:
        m+=1
print(m) 