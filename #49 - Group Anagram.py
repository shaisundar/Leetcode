class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=collections.defaultdict(list)
        for i in strs:
            a = dict(Counter(i))
            tmp = tuple(sorted(a.items()))
            res[tmp].append(i)
        
        res2=[]
        for i in res:
            res2.append(res[i])
        
        return(res2)
