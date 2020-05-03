from collections import Counter
class Solution:
    def canConstruct(self, ransomNote, magazine):
        c_r=Counter(ransomNote)       
        for i,j in c_r.items():
            if magazine.count(i)<j:
                return False
        return True
      
   
        

