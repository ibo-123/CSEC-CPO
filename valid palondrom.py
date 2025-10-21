class Solution:
    def isPalindrome(self, s: str) -> bool:
        A="QWERTYUIOPASDFGHJKLZXCVBNM"
        a="qwertyuiopasdfghjklzxcvbnm"
        n="1234567890"
        m=""
        for i in s:
            if i in a or i in A or i in n:
                m+=i
        r=m[::-1]
        return r.lower()==m.lower()
