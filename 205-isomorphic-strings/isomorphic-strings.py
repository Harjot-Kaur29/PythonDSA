class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d1 = {}
        d2 = {}
        for i in range(len(s)):
            c1,c2 = s[i],t[i]
            if c1 not in d1:
                d1[c1] = c2
            else:
                if d1[c1]!=c2:
                    return False
                    
            
            if c2 not in d2:
                d2[c2] = c1
            else:
                if d2[c2]!=c1:
                    return False
        return True