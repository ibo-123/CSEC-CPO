m = input()
index_ = 0
list_ = [0]
num = 0
while index_ < len(m): 
       if index_ +1 < len(m) :    
                if m[index_] == m[index_ +1]:
                        num+=1
                        list_.append(num)
                else:
                        list_.append(num)
                index_ +=1
       else:
               list_.append(num)
               index_ +=1   
for i in range(int(input())):
        first , second = map(int, input().split())
 
        if  list_[second-1] == list_[second]:
                print(list_[second] - list_[first-1])
        else:
                print(list_[second] - list_[first-1] -1)
