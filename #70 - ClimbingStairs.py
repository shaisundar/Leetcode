class Solution:
    def climbStairs(self, n: int) -> int:
        res=0
        d = [0,1,2]
        if n==1:
            return 1
        if n==2:
            return 2
        for i in range(3,n+1):
            d.append(d[i-1]+d[i-2])
        
        return(d[n])
     
    # Number of ways to reach the n'th step = (number of ways to reach the (n-1)th step + number of ways to reach the (n-2)th step).
    # In order to make this more optimal, we store the number of ways to reach each step in an array, rather than recurvesly calling the function for each step.
    
