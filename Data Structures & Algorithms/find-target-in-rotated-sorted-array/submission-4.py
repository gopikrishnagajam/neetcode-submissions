class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1
        while i<j:
            mid = (i+j)//2
            if nums[mid]>nums[j]:
                i =mid +1
            else:
                j=mid
        pivot = i

        def bs(i , j):
            while i<=j:
                mid  =(i+j)//2
                if target>nums[mid]:
                    i = mid+1
                elif target<nums[mid]:
                    j=mid-1
                else:
                    return mid
            return -1
            
        if pivot ==0:
            return bs(0,len(nums)-1)
        elif nums[0]<= target <= nums[pivot-1]:
            return bs(0,pivot-1)
        elif nums[pivot] <= target <=nums[-1]:
            return bs(pivot, len(nums)-1)
        else:
            return -1
        
