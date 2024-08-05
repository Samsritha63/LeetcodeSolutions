class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={")":"(","]":"[","}":"{"}
        for b in s:
            if b in closeToOpen:
                if stack and stack[-1]==closeToOpen[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False
        