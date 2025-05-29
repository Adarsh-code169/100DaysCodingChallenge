class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If length is less than or equal to 2, all elements can stay
        if len(nums) <= 2:
            return len(nums)
        
        # write_index points to where we write the next allowed element
        write_index = 2
        
        # Start reading from the 3rd element (index 2)
        for i in range(2, len(nums)):
            # Compare current number with the number two places before the write_index
            # If different, it means we haven't yet added this element twice, so we add it
            if nums[i] != nums[write_index - 2]:
                nums[write_index] = nums[i]
                write_index += 1
        
        return write_index