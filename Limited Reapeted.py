def feasible(s , a , k , p):
    n = len(a)
    i = 0 
    segment = 0
    
    while i < n:
        
        if a[i] > p and s[i] =="R":
            i+=1
            continue
        need = False
        j = i
        while j < n and not(a[j] > p and s[j] == "R"):
            if s[j] == "B" and a[j] > p:
                need = True
            j+=1
        if need:
            segment+=1
            if segment > k:
                return False
        i = j
    return segment <= k
def solve(s , a , k):
    l , r = 0 , max(a)  
    while l <= r:
        mid = (l+r)//2
        if feasible(s , a , k , mid):
            r = mid - 1
        else:
            l = mid + 1
    return r + 1
for i in range(int(input())):
    n , k = map(int,input().split())   
    s = input() 
    a = list(map(int,input().split())) 
    print(solve(s , a , k))
