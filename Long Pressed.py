class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        left = 0
        right = 0
        prev = ""
        while right < len(typed) and left < len(name):
            if name[left] == typed[right]:
                prev = name[left]
                left+=1
                right+=1
            elif name[left] != typed[right] and typed[right] == prev:
                right+=1
            else:
                return False
        print(typed[right:] , right,left,prev)
        if left == len(name):
            if right < len(typed) and len(set(typed[right:])) == 1 and typed[-1] == prev:
                return True
            elif right== len(typed) :
                return True
            else:
                return False
        return False

