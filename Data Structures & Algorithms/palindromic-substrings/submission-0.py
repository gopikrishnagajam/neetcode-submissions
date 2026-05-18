class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            oddlen = 1
            while i-oddlen >=0 and i+oddlen <len(s) and s[i-oddlen] == s[i+oddlen]:
                oddlen+=1
            res+= oddlen
            evenlen = 0
            while i-evenlen>=0 and i+1+evenlen<len(s) and s[i-evenlen] == s[i+1+evenlen]:
                evenlen+=1
            res+=evenlen
        return res
            

                