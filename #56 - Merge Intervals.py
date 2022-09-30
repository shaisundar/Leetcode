class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:(i[0],i[1]))
        print(intervals)

        prevstart=intervals[0][0]
        prevend=intervals[0][1]
        res=[]

        for start,end in intervals[1:]:
            if start<=prevend:
                prevend=max(prevend,end)
                continue
            res.append([prevstart,prevend])
            prevstart=start
            prevend=end
        res.append([prevstart,prevend])
        return(res)
        
    # sort the array , start taking first element
    # if the start of the next element if smaller than prevend, merge them and skip that loop.
    # finally just append them to result
