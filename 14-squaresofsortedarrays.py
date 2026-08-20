class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            num = nums[i]*nums[i]
            result.append(num)
        
        result.sort()
        return result