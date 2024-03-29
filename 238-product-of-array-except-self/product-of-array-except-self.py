class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n

        for i in range(1,n):
            answer[i] = answer[i-1]*nums[i-1]

        suffix = 1
        for j in range(n-1,-1,-1):
            answer[j] = answer[j] * suffix
            suffix = suffix * nums[j]

        return answer