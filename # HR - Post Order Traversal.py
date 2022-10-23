import collections
res=[]
def postOrder(root):
    #Write your code here
    def dfs(root):
        if root.left: dfs(root.left)
        if root.right: dfs(root.right)
        res.append(root.info)
    dfs(root)
    for i in res:
        print(i,end=" ")
        
# post order = left, right, root
# Always DFS.
