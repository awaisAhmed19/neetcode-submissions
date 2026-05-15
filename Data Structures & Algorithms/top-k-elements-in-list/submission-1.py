class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk={}
        for i in range(len(nums)):
            if nums[i] not in topk:
                topk.setdefault(nums[i],1)
            else:
                topk[nums[i]]+=1
        tpk= sorted(topk.items(), key = lambda kv: kv[1],reverse=True)
        return [tpk[i][0] for i in range(k)]