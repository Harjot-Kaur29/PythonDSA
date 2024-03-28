class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        end =  0
        maxlen = 0
        d = {}
        for start , value in enumerate(nums):
            if value not in d:
                d[value] = 0
            d[value] +=1

            while d[value] > k:
                d[nums[end]] -=1
                end +=1

            maxlen = max(maxlen, start-end+1)
        return maxlen