class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in range(0,len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                return True
        return False

        