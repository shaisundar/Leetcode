class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hm=collections.defaultdict(lambda:0)
        res=[]
        for i in nums:
            hm[i]+=1
            if hm[i]==2:
                res.append(i)
        for i in range(1,len(nums)+1):
            if hm[i]==0:
                res.append(i)
        return(res)
        
# loop once to set hashmap
# loop next time to check hashmap for missing element
