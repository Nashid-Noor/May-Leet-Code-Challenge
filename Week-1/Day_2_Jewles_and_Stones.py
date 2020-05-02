class Solution:
    def numJewelsInStones(self, J, S) :
        c=0
        for i in range(len(J)):
            c+=S.count(J[i])           
        return c
