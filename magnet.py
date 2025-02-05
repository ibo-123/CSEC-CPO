x=int(input())
p=input()
m=1
for i in range(x-1):
    y=input()
    if p==y:
        p=y
    else:
        m+=1
        p=y
print(m) 