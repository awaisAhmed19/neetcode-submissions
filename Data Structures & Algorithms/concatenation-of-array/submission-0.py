class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # need a list initilized which is the twice the size of nums
        ans=[0]*(len(nums)*2)
        n=len(nums)
        # print(ans)
        for i in range(n):
            ans[i]=nums[i]
            ans[i+n]=nums[i]
        return ans