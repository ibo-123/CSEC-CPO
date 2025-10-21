class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        left = 0
        right = 0
        coun = 0
        g = sorted(g)
        s = sorted(s)
        while left < len(g) and right < len(s):
            if g[left] <= s[right]:
                left +=1
                right+=1
                coun+=1
            else:
                right+=1
        return coun
