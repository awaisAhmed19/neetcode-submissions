class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp=strs[0]
        # print(strs[1])
        for i in range(1,len(strs)):
            curr=strs[i]
            if curr=="":
                return ""
            n=min(len(curr),len(lcp))
            for j in range(0,n):
                print(curr)
                if len(curr)<len(lcp) and curr==lcp[0:len(curr)]:
                    lcp=curr
                if j<len(curr) and j < len(lcp) and lcp[j]!=curr[j]:
                    lcp=lcp[0:j]
        return lcp
                
    
                    