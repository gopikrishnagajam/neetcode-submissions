class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        stack  = []
        stack.append(intervals[0])
        for interval in intervals:
            current = stack.pop()
            if current[1]>=interval[0]:
                if current[1]>=interval[1]:
                    stack.append(current)
                else:
                    stack.append([current[0],interval[1]])
            else:
                stack.append(current)
                stack.append(interval)
        return stack