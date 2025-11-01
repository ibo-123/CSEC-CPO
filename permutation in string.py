class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        first = Counter()
        for i in s1:
            first[i]+=1
        second = Counter(s2[:len(s1)])
        left = 0
        right = len(s1)
        while right < len(s2):
            if first == second:
                return True
            second[s2[left]]-=1
            second[s2[right]]+=1
            right+=1
            left+=1
        if first == second:
                return True
        return False
