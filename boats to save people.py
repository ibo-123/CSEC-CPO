
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = sorted(people)
        right = len(n)-1
        left = 0
        coun = 0
        length = 0
        while left< right :
                if n[left] + n[right]<= limit:
                        right-=1
                        left+=1
                        coun+=1
                        length +=2
                else:
                        right-=1
                        coun+=1
                        length+=1
        if length < len(n):
                        coun+=1
        return coun 
