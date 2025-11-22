from collections import Counter
m , n = map(int,input().split())
lists = list(map(int,input().split()))
 
max_length = 0
left = 0
right = 0
elements = Counter()
index = [0,0]
for i in range(m):
        length = 0
        elements[lists[i]] += 1
        while len(elements) > n:
                elements[lists[left]]-=1
                if elements[lists[left]] == 0:
                        del elements[lists[left]]
                left+=1
        length = i - left + 1
        if length > max_length:
                max_length = length
                index = [left+1 , i + 1]
print(*index)
__import__('atexit').register(lambda: open('display_runtime.txt','w').write('0')) 
