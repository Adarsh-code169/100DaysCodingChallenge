class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # stores number -> index mapping
        
        for i, num in enumerate(nums):
            complement = target - num  # number we need to find
            
            if complement in num_map:  # if complement already seen
                return [num_map[complement], i]
            
            num_map[num] = i  # store current number with its index
