class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2={v:k for k,v in enumerate(nums)}
        
        for i in range(len(nums)):
            diff = target -nums[i]
            if diff in nums:
                if i!=nums2[diff]:
                    return [i,nums2[diff]]
        return []