class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def rec(i , arr, total):
            if total == target:
                res.append(arr[:])
                return
            if i>=len(nums) or target<total:
                return
            rec(i,arr+[nums[i]],total+nums[i])
            rec(i+1 , arr ,total)
            return
        rec(0,[],0)
        return res