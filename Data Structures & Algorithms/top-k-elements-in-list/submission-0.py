class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        knums = {}
        result = []
        for num in nums:
            if num in knums:
                knums[num] += 1
            else:
                knums[num] = 1
        
        i = 0
        while i < k:
            top_k = max(knums, key=knums.get)
            result.append(top_k)
            knums.pop(top_k, None)
            i += 1

        return result

        