class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
        print(stones)
        heapq.heapify(stones)
        while len(stones)>1:
            x,y=heapq.nsmallest(2,stones)
            heapq.heappop(stones)
            heapq.heappop(stones)
            if x==y:
                pass
            else:
                heapq.heappush(stones,abs(x-y)*-1)
            print(stones)
        
        if len(stones)==0:
            return 0
        else:
            return stones[0]*-1
            
    
    # Use a heapq to continuously take out top 2 elements, and push the difference to maintain the order. 
