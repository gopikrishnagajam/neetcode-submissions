class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        i=0
        while i<len(intervals) and intervals[i][1]<newInterval[0]:
            output.append(intervals[i])
            i+=1
        output.append(newInterval)
        if i==len(intervals):
            return output
        
        for j in range(i, len(intervals)):
            c = output.pop()
            if intervals[j][0]<=c[0] and intervals[j][1]>=c[1]:
                output.append(intervals[j])
            elif intervals[j][0]>=c[0] and intervals[j][1]<=c[1]:
                output.append(c)
            elif intervals[j][0]> c[1]:
                output.append(c)
                output.append(intervals[j])
            else:
                output.append([min(c[0],intervals[j][0]),max(c[1],intervals[j][1])])
        return output
        