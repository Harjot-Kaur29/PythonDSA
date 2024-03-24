class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortorise = hare = nums[0]

        while(True):
            tortorise = nums[tortorise]
            hare = nums[nums[hare]]
            if (hare == tortorise):
                break

        tortorise = nums[0]
        while tortorise != hare:
            tortorise = nums[tortorise]
            hare = nums[hare]

        return tortorise
        