class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n // 4

        def find_left(arr, target):
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        def find_right(arr, target):
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        for i in [n // 4, n // 2, 3 * n // 4]:
            elem = arr[i]
            left = find_left(arr, elem)
            right = find_right(arr, elem)
            if right - left > threshold:
                return elem
            