class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s = sorted(skill)
        left = 1
        right = len(skill)-2
        multi = s[left-1] + s[right+1]
        sum_ = s[left-1] * s[right+1]
        while right>left:
            n = s[left] * s[right]
            o = s[left]+s[right]
            
            if multi == o :
                    sum_+=n
            else:
                    sum_ = -1
                    break
            right-=1
            left +=1
        return sum_
