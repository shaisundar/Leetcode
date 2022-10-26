class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hm={0:0}
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            if s%k not in hm:
                hm[s%k]=i+1
                #print(hm)
            elif i-hm[s%k]>=1:
                return True
        #print(hm)
        return False
      
  # create hashmap of reminder
  # if you see the same reminder again, it means everything in between is a multiple of k. 
  # if the length of that is greater than 1, then return True
