class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        stack =deque()
        res = 0
        for char in s:
            if char not in count:
                count.add(char)
                stack.append(char)
            else:
                res = max(res, len(stack))
                while stack and stack[0] != char:
                    count.remove(stack.popleft())
                
                stack.popleft()
                stack.append(char)
        return max(res,len(stack))
                    
                 