class Solution:
    def countBits(self, n: int) -> List[int]:
        res =[]
        def bitcount(k):
            res = 0
            for i in range(32):
                if (1 << i) & k:
                    res+=1
            return res
        for i in range(n+1):
            res.append(bitcount(i))
        return res