# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res=0
        self.q=[]
        def dfs(root,min1,max1,res):
            if not root:
                return res
            cur=root.val
            min1=min(cur,min1)
            max1=max(cur,max1)
            res=max(res,abs(cur-min1),abs(cur-max1))
            if root: self.q.append(dfs(root.left,min1,max1,res))
            if root: self.q.append(dfs(root.right,min1,max1,res))
        dfs(root,root.val,root.val,0)
        
        x=0
        for i in self.q:
            if i != None:
                x=max(x,i)
        return x
        
        
   # Do DFS, just keep track of max and min for each branch. keep counting res and adding it to list
   # Then just take max of this list
