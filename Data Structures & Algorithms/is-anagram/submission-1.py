class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = {}
        for char in s:
            res[char] = 1+res.get(char ,0)
        for char in t:
            if char not in res:
                return False
            res[char]-=1
            if res[char]==0:
                del res[char]
        if res:
            return False
        return True