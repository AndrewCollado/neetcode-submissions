class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for num in numbers:
            diff = target - num
            if diff in numbers and diff != num:
                return [numbers.index(num) + 1, numbers.index(diff) + 1]