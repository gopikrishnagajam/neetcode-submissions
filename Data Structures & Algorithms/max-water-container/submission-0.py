class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, n, r= 0, len(heights), len(heights)-1
        res = 0
        while l<r:
            res = max(res, min(heights[l],heights[r])*(r-l))  
            print(res)
            if heights[l]<=heights[r]:
                temp =heights[l]
                while l<n and heights[l]<=temp:
                    l+=1
            else:
                temp =heights[r]
                while r>0 and heights[r]<=temp:
                    r-=1
        return res