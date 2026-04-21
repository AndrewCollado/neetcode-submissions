class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for i in range(len(nums))]
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            prefix = prefix * nums[i]
            if i+1 != len(nums):
                result[i+1] = prefix * result[i+1]
                  
            result[-(i+1)] = result[-(i+1)] * postfix
            postfix = postfix * nums[-(i+1)]    

        return result

        
            
