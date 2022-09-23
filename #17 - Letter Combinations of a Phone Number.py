class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        let=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        
        if digits=="":
            return ([])
        
        q = collections.deque()
        res=[]
        for i in let[int(digits[0])]:
            q.append(i)
        
        x=0
        
        while q:
            node=q.popleft()
            if len(node)==len(digits):
                res.append(node)
                continue
            try:
                for i in let[int(digits[len(node)])]:
                    q.append(node+i)
                    print(q)
            except:
                pass
        
        return(res)
            
            
          
 # solved using bfs. 
 # maintain a queue - pop from left, add new letetrs to it, append it to queue
 # while popping if the numbers of letters= desired length, just add it to res.
