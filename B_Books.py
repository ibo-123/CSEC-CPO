n , t = map(int,input().split())
books = list(map(int,input().split()))

count = 0
left = 0
right = 0
current_sum = 0
max_books = 0
while right < n:
        if current_sum + books[right] <= t:
                current_sum+=books[right]
                right+=1
                count+=1
        else:
                current_sum-=books[left]
                left+=1
                count-=1
        max_books = max(max_books, count)       

print(max_books)
                