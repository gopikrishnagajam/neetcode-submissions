class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        if nums[0]>0 or n==1:
            dp[0]=True
        else:
            return False
        for i in range(n):
            if dp[i]:
                for j in range(nums[i]+1):
                    if j+i<n:
                        dp[j+i] =True
        return dp[n-1]
