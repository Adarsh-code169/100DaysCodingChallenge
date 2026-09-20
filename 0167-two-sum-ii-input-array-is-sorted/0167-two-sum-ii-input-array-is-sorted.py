class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        L=0
        R=len(numbers)-1
        
        while L<R:
            curr_sum=numbers[L]+numbers[R]

            if curr_sum==target:
                return [L+1,R+1]
            elif curr_sum>target:
                R=R-1
            else:
                L=L+1

        
        