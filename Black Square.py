y=list(map(int,input().split()))
x=input()
v=[]
v.extend(x)
s=0
for i in v:
    s+=y[int(i)-1]
print(s)    