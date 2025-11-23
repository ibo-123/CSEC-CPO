class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        index=0
        m = ""
        prefix = [0]*(len(s)+1)
        strings = []
        for i in s:
            strings.append(ord(i)) 
        for i in shifts:
            start=i[0]
            direction=i[2]
            if direction == 0:
                direction = -1
            prefix[start]+= direction
            prefix[i[1]+1] -= direction



        for i in range(1,len(s)):
            prefix[i] = prefix[i] + prefix[i-1]
        print(prefix)

        for i in range(len(s)):
            strings[i] = (strings[i] + prefix[i] - ord('a'))%26 + ord('a')


        ans = []
        for i in range(len(s)):
            ans.append(chr(strings[i]))
        return "".join(ans)

        
            
