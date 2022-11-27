class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        res=0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dp[i]=dp[i-1]+1
                res+=dp[i]
        return(res)
      
      
  # Just maintain a dp and add to it only if more than 2 elements have the same difference. 
  # We can even do this without an array, using just a var to store the prev dp value. 
