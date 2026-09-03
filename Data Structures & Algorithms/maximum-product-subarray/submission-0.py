class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cMin , cMax = 1,1

        for num in nums:
            tmp = cMax * num
            cMax = max(num*cMax , num*cMin , num)
            cMin = min(tmp , num* cMin ,num)
            res = max(res,cMax)
        return res