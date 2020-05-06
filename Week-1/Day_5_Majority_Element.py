class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s=set(nums)
        m=0
        for i in s:
            if nums.count(i)>m:
                m=nums.count(i)
                highest=i
        return highest
        
        
