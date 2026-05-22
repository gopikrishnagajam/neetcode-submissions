class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse = True ))
        res = []
        for item in sorted_count:
            if k>0:
                res.append(item) 
                k-=1
            else:
                return res
        return res    