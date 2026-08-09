from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        rset = set(nums)
        result = []
        for i in range(1,len(nums)+1):
            if i not in rset:
                result.append(i)

        
        return result
            