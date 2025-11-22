class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        left = 0
        right = 0
        final = []
        while right < len(a) and left < len(b):
            start = max(a[right][0] , b[left][0])
            end = min(a[right][1] , b[left][1])
            if start<=end:
                final.append([start , end])
            if a[right][1] < b[left][1]:
                right +=1
            else:
                left+=1
        return final

            
        
                    
