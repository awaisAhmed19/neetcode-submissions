class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        suffix=[0]*len(nums)
        suffix[len(nums)-1]=1
        prefix[0]=1
        # print(prefix)
        for i in range(1,len(nums)):
            prefix[i]=nums[i-1]*prefix[i-1]
        # print(prefix)
        # print(suffix)
        for j in range(len(nums)-2,-1,-1):
            suffix[j]=nums[j+1]*suffix[j+1]
        # print(suffix)

        res=[]
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i])
        return res