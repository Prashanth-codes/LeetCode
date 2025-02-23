# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        root=TreeNode(preorder[0])
        if len(preorder)==1:
            return root
        l=preorder[1]
        s=postorder.index(l)+1
        root.left=self.constructFromPrePost(preorder[1:s+1],postorder[:s])
        root.right=self.constructFromPrePost(preorder[s+1:],postorder[s:-1])
        return root