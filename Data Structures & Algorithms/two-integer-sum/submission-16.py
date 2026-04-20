class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        i = 0
        j = 1
        while i < len(nums):
            while j < len(nums):
                if nums[i] + nums[j] == target and i != j:
                    result.append(i)
                    result.append(j)
                j += 1
            i += 1
            j = 1
        
        return list(set(result))
        