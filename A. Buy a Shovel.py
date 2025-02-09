x=list(map(int,input().split()))
k=str(x[0])
s=1
if int(k)%10==0 or int(k[-1])==x[1]:
    print(1)
else :
      while not(int(k)%10==0 or int(k[-1])==x[1]):
           k=x[0]
           s+=1
           k=int(k)
           k*=s
           k=str(k)
      print(s)
    