from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for indx,value in enumerate(nums):
            diff = target -value
            if diff in hash_map:
                return(indx,hash_map[diff])
            hash_map[value] = indx