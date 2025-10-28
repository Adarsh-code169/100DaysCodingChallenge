class Solution(object):
    def longestConsecutive(self, nums): 
        if not nums:
            return 0

        nums.sort()   
        Yo = 1        
        l = 1      

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  
            elif nums[i] == nums[i - 1] + 1:
                l += 1 
            else:
                Yo = max(Yo, l)  
                l = 1

        Yo = max(Yo, l) 
        return Yo
