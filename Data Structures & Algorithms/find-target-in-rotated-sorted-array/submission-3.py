class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1
        while i<j:
            mid = (i+j)//2
            if nums[mid]>nums[j]:
                i =mid +1
            else:
                j=mid
        left = nums[:i]
        right = nums[i:]
        print(left)
        def bs(arr  ,target):
            i,j = 0, len(arr)-1
            while i<j:
                mid  =(i+j)//2
                if target>arr[mid]:
                    i = mid+1
                elif target<arr[mid]:
                    j=mid-1
                else:
                    return mid
            if i <len(arr) and arr[i]==target:
                return i
            return -1
        l = bs(left ,target)
        r = bs(right ,target)
        if l != -1:
            return l
        elif r!= -1:
            return len(left) +r
        else:
            return -1
