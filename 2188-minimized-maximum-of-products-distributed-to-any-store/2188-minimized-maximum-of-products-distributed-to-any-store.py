class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def is_possible(mid):
            count = 0
            for q in quantities:
                count += (q + mid - 1) // mid
            return count <= n

        low = 1
        high = max(quantities)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
        