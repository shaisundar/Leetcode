class Solution:
    def reverseWords(self, s: str) -> str:
        x=0
        q=collections.defaultdict(list)
        for i in s:
            if i==" ":
                x+=1
                continue
            q[x].append(i)

        res=[]
        for i in range(x,-1,-1):
            if q[i]==[]:
                continue
            res.append(''.join(j for j in q[i]))
            print(res)
        res2 = (' '.join(j for j in res))
        return(res2.strip())

      
  # Brute force in O(N). 
  # push into q, spliting by spaces. 
  # take from q backwards and put int string. 
