class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        celeb=[0]*(N+1)
        for i,j in trust:
            celeb[i]-=1
            celeb[j]+=1
        for i in range(1,len(celeb)):
            if celeb[i]==N-1:
                return i
        return -1
            
        
        
            
        
      
            
            
        
