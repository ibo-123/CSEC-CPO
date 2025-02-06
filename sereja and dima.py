n = int(input())  # Number of cards
c= list(map(int, input().split()))
s=0
d=0
if n%2==0:
    for i in range(int(n/2)):
        if c[0]>c[-1]:
            s+=c[0]
            c.pop(0)
        else:
            s+=c[-1]
            c.pop()  
        if c[0]>c[-1]:
            d+=c[0]
            c.pop(0)
        else:
            d+=c[-1]
            c.pop() 
else:
    for i in range(int(n/2)):
        if c[0]>c[-1]:
            s+=c[0]
            c.pop(0)
        else:
            s+=c[-1]
            c.pop()  
        if c[0]>c[-1]:
            d+=c[0]
            c.pop(0)
        else:
            d+=c[-1]
            c.pop()
    s+=c[0]             
print(s,d)                 