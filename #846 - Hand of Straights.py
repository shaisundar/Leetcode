
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand=sorted(hand)
        hm=collections.defaultdict(lambda:0)
        for i in hand:
            hm[i]+=1

        res=[]
        while hand:
            start=hand[0]
            hm[hand[0]]-=1
            tmpset=[hand[0]]
            for i in range(start+1,start+groupSize):
                if hm[i]>=1:
                    hand.remove(i)
                    tmpset.append(i)
                    hm[i]-=1
                else:
                    return False
            hand=hand[1:]
            res.append(tmpset)
        #for printing the resulting groups - print(res)
        return True


# Approach
# We sort the list in ascending order
# We keep a counter of all existing elements
# For each element in the list we check if the next (groupSize) consequtive elements are present (by checking the counter).
# If they are present, we remove them from the original list
# (If consequtive elements are not found, return false directly)

# Now we iterate this until the list is empty.

# Follow Up
# In this approach we can even print the resulting list ("res" array in the code)

# Complexity
# Time complexity:
# $O(N log N + NW) (I guess)
