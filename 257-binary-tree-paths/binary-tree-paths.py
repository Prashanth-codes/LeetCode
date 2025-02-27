# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def backtrack(r,p):
            if r.left==None and r.right==None:
                ans.append(p[:len(p)-2])
                return
            for v in [r.left,r.right]:
                if v:
                    backtrack(v,p+str(v.val)+"->")
        backtrack(root,str(root.val)+"->")
        return ans