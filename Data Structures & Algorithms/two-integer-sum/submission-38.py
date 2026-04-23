class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        result = {}

        while i < len(nums):
            difference = target - nums[i]
            if difference in result:
                return [result[difference], i]
            result[nums[i]] = i
            i += 1
        
        return []