class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = -100000
        remove = 0
        for start, finish in intervals:
            if start < end:
                remove += 1
            else:
                end = finish
        return remove
            