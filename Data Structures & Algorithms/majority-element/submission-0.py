class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        n=len(nums)
        for i in nums:
            if i not in count:
                count.setdefault(i,1)
            else:
                count[i]+=1
        res=0
        for key,val in count.items():
            if val>=n/2:
                res=key
        return res