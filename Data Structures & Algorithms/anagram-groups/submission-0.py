class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for word in strs:
            result.setdefault("".join(sorted(word)),[]).append(word)
        # print(result)
        res=[val for k,val in result.items()]
        # print(res)
        return res