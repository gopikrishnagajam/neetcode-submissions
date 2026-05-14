"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end , n = [],[],len(intervals)
        for num in intervals:
            start.append(num.start)
            end.append(num.end)
        start.sort()
        end.sort()
        s,e,count,res  = 0,0,0,0
        while s<n:
            while s<n and start[s]<end[e]:
                s+=1
                count+=1
            e+=1
            res = max(res,count)
            count-=1
        return res
