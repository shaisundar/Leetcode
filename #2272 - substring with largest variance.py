class Solution:
    def solveone(self,a,b,s):
        maxvar=0
        var=0
        startb=False
        hasb=False
        for c in s:
            if c==a:
                var+=1
            if c==b:
                hasb=True
                if startb and var>=0:
                    startb=False
                elif var-1<0:
                    startb=True
                    var=-1
                else:
                    var-=1
        
            if hasb:
                maxvar=max(maxvar,var)
        return maxvar



    def largestVariance(self, s: str) -> int:
        maxvar=0
        hm = set(s)
        for i in hm:
            for j in hm:
                tmp = self.solveone(i,j,s)
                maxvar=max(maxvar,tmp)
        return maxvar        
      
      
   # We need to check for each of charecter pairss present in the string.
  # The checking - 
  #         https://leetcode.com/problems/substring-with-largest-variance/discuss/2579146/%22Weird-Kadane%22-or-Intuition-%2B-Solution-Explained
