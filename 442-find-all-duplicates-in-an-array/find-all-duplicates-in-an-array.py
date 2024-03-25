class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        for num in nums:
            abs_index = abs(num) -1
            
            if nums[abs_index] < 0:
                duplicates.append(abs_index + 1)
            
            else:
                nums[abs_index] *= -1
        
        return duplicates
        