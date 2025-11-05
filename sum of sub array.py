m , n = map(int, input().split())
arr = list(map(int, input().split()))

coun = 0
left = 0
right = 0
current_sum = 0
while right < m:
        current_sum+=arr[right]
        if current_sum == n:
                coun+=1
        elif current_sum > n:
                while current_sum > n and left<=right:
                        current_sum-=arr[left]
                        left+=1
                if current_sum == n:
                        coun+=1
        right+=1
        
print(coun)
                
                
