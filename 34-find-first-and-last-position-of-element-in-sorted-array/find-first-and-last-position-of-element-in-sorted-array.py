class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_occurence = -1
        last_occurence = -1

        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                first_occurence = mid
                r = mid-1
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1


        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                last_occurence = mid
                l = mid+1
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return (first_occurence,last_occurence)


        