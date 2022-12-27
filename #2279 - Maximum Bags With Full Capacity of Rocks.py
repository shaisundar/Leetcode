class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], extra: int) -> int:
        rem=[]
        for i in range(len(rocks)):
            rem.append(capacity[i]-rocks[i])
        rem=sorted(rem)

        res=0
        for i in rem:
            if extra==0 or i>extra:
                break
            if i==0:
                res+=1
                continue
            else:
                extra-=i
                res+=1
        return(res)
      
# Get a reminder of the rocks and sort them in ascending order. 
# Then try to fill these up..
# highest you can go or until the next lowest bag is lesser than than the max is the answer. 
