"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        start, end  =[], []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        i=0
        for e in end:
            conflict =0
            while i <len(start) and start[i]<e:
                i+=1
                conflict+=1
            if conflict >1:
                return False
        return True

    
            