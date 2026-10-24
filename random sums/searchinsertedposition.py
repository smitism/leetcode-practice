class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        p = 0
        while p<len(nums):
            
            if nums[p]>=target:
                return p
            p += 1
        return p