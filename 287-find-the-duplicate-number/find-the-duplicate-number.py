class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        sum_natural = (n*(n-1)//2)
        sum_2 = 0
        diff = 0
        nums.sort()


        for i in range(0,n):
            if nums[i] == nums[i-1]:
                return nums[i]
            else:
                sum_2 += nums[i]
                diff = sum_2 - sum_natural

        return diff
        