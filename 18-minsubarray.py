from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        result = 10^5
        total = 0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                result = min(result , r-l+1)

                total -= nums[l]
                l+=1

        if result == 10^5:
            return 0 
        else:
            return result