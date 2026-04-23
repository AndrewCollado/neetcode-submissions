class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        print(nums)
        count = 1
        last = nums[0]
        groups = {}
        for num in nums: 
            if num == last + 1:
                last = num
                count += 1
                groups[count] = count
            else:
                print(count)
                if count > 1:
                    if num == last:
                        continue
                    else:
                        last = num
                        count = 1
                        groups[count] = count
                last = num
        
        count = max(groups.values()) if len(groups) > 0 else 1
        
        return count