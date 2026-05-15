class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i= 0
        count={}
        maxf =0
        res=1
        for j in range(len(s)):
            if s[j] in count:
                count[s[j]]+=1
            else:
                count[s[j]]=1
            maxf = max(maxf, count[s[j]])
            while (j-i+1)-maxf >k:
                count[s[i]]-=1
                i+=1
            res = max(res, j-i+1)
        return res
