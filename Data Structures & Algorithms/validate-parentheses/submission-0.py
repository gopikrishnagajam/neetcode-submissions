class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {'(':')', '{':'}' ,'[':']'}
        stack = []
        for char in s:
            if char in bracket:
                stack.append(char)
            elif stack and bracket[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return True if not stack else False 
