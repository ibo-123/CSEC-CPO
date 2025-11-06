class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = defaultdict(int)
        
        have, need = 0, len(target)
        result, result_length = [0,0], float('inf')
        
        left, right = 0,0
        
        while right < len(s):
            window[s[right]] += 1
            
            if window[s[right]] == target[s[right]]:
                have += 1
            
            while have == need:
                if result_length > right - left + 1:
                    result_length = right - left + 1
                    result = [left,right]
                
                window[s[left]] -= 1
                
                if window[s[left]] < target[s[left]]:
                    have -= 1
                
                left += 1
            
            right += 1
        
        if result_length != float('inf'):
            l, r = result
            return s[l:r+1]
        
        return ""
