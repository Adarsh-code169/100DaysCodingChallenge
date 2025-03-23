class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def time_taken(speed):
            time = 0
            for i in range(len(dist) - 1):
                time += math.ceil(dist[i] / speed)
            time += dist[-1] / speed
            return time

        if hour <= len(dist) - 1:
            return -1

        low, high = 1, 10**7
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if time_taken(mid) <= hour:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
            