x=int(input())
y=input()
z=[]
z.extend(y)
l=[]
for i in range(len(z)-1):
    if y[i]==y[i+1]:
        l.append(y[i])
    else:
        continue
print(len(l))            