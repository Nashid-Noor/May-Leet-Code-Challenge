from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=Counter(s)
        for i in c:
            if c[i]==1:            
                return s.find(i)
        return -1
        
