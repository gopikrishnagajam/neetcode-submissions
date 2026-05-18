class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set(nums)
        if len(nums)==len(res):
            return False
        return True