class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        maxlen = 0
        count = 0
        start = 0
        end = 0
        n = len(nums)

        while end<n:
            if nums[end] == max_element:
                maxlen+=1
            while maxlen == k:
                count += (n - end)
                if nums[start] == max_element:
                    maxlen -=1
                start +=1
            end+=1
        return count
            
                    
               
        