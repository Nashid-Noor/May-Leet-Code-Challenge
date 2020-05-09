class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<2:
            return True
        l,r=1,num//2
        while l<=r:
            mid=l+(r-l)//2
            sqr=mid*mid
            if sqr==num:
                return True
            elif sqr>num:
                r=mid-1
            else:
                l=mid+1
        return False
