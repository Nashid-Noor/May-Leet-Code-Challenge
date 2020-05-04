class Solution:
    def findComplement(self, num) :
        l=[]
        b_num=str(bin(num))[2:] 
        for i in  b_num:
            l.append(i)
        for i in range(len(l)):
            if l[i]=='1':
                l[i]='0'
            else:
                l[i]='1'
        d=''.join(l)        
        return int(d,2)
        
        
            
            
