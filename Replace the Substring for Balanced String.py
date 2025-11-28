class Solution:
    def balancedString(self, s: str) -> int:
        counting = Counter(s)
        n = len(s)//4
        m = Counter()
        m["Q"] = counting["Q"]-n
        m["W"] = counting["W"]-n
        m["R"] = counting["R"]-n
        m["E"] = counting["E"]-n
        min_ = float("inf")
        if m == {"Q":0 , "R" : 0 , "W" : 0, "E" : 0}:
            return 0
        l , r = 0 , 0
        new = Counter()
        while r < len(s):
            new[s[r]]+=1
            while all(new[c] >= m[c] for c in m ):
                min_ = min(min_ , r-l+1)
                new[s[l]]-=1
                l+=1
            r+=1
        return min_
