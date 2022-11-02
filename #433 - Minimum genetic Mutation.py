class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = collections.deque()
        q.append((start,0))
        seen=[]

        while q:
            #print(q)
            node, step = q.popleft()
            if node==end:
                return step
            else:
                for i in "ACGT":
                    for j in range(len(node)):
                        tmp = node[:j]+i+node[j+1:]
                        print(tmp)
                        if tmp not in seen and tmp in bank:
                            q.append((tmp,step+1))
                            seen.append(tmp)
        return -1
      
      
 # Do a BFS
 # Change each letter and see if it has already been seen or is present in the bank
 # if the leaf is equal to end, return the number of steps it took. 
