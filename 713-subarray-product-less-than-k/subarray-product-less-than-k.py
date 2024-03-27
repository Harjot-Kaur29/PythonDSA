class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        n= len(nums)
        start = 0
        end = 0
        prod = 1
        count = 0
        #expansion
        while end < n:
            prod = prod*nums[end]
            while prod>=k:
                prod = prod/nums[start]
                start+=1
            count = count + (end-start+1)
            end+=1

        return count