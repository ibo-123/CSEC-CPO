class Solution:
    def minimumSteps(self, s: str) -> int:
        num_one = 0
        coun = 0
        bulb = False
        for i in range(len(s)):
            if s[i] == "0" :
                coun+= num_one
            elif s[i] == "1":
                num_one+=1
        
        
        return coun
