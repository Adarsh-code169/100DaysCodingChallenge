from collections import defaultdict
import bisect

class RangeFreqQuery:
    def __init__(self, arr):
        self.pos_map = defaultdict(list)  # Dictionary to store indices of each value
        for idx, num in enumerate(arr):
            self.pos_map[num].append(idx)

    def query(self, left, right, value):
        if value not in self.pos_map:
            return 0  # Value not present in the array
        
        indices = self.pos_map[value]
        left_idx = bisect.bisect_left(indices, left)   # First index ≥ left
        right_idx = bisect.bisect_right(indices, right)  # First index > right
        
        return right_idx - left_idx  # Count of occurrences in the range