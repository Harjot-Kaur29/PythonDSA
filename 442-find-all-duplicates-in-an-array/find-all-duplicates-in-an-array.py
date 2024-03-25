class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        lst = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
         
        for i,count in d.items():
            if count>1:
                lst.append(i)
        if lst:
            return sorted(lst)
        
        else:
            return []
            
        