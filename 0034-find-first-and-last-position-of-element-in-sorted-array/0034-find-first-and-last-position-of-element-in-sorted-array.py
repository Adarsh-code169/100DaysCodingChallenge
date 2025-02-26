class Solution:
    def searchRange(self, nums, target):
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            first_index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    first_index = mid
                    right = mid - 1  # Keep searching left for the first occurrence
            return first_index

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            last_index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    last_index = mid
                    left = mid + 1  # Keep searching right for the last occurrence
            return last_index

        first = find_first(nums, target)
        if first == -1:
            return [-1, -1]  # Target not found
        last = find_last(nums, target)
        return [first, last]

# Example usage:
sol = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(sol.searchRange(nums, target))  # Output: [3, 4]