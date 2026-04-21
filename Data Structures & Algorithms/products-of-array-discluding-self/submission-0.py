class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
                postfix[-(i+1)] = nums[-(i+1)]
                continue

            prefix[i] = prefix[i-1] * nums[i] 
            #idx 0 = 1
            #idx 1 = 1 * 2 = 2
            #idx 2 = 2 * 4 = 8
            #idx 3 = 8 * 6 = 48

            postfix[-(i+1)] = postfix[-(i+1) + 1] * nums[-(i+1)]
            # idx 3 = 6
            # idx 2 = 4 * 6 = 24
            # idx 1 = 24 * 2 = 48
            # idx 0 = 48 * 1 = 48

        for i in range(len(nums)):
            if i == 0:
                out = 1 * postfix[i+1]
                result.append(out)
                continue
            if i + 1 == len(nums):
                out = prefix[i-1] * 1
                result.append(out)
                continue
            
            out = prefix[i-1] * postfix[i+1]
            result.append(out)
        
        return result

        
            
