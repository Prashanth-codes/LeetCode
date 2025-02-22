# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        st=[]
        i,n=0,len(traversal)
        while i<n:
            d=0
            while i<n and traversal[i]=='-':
                d+=1
                i+=1
            s=i
            while i<n and traversal[i].isdigit():
                i+=1
            num=int(traversal[s:i])
            nd=TreeNode(num)
            while len(st)>d:
                st.pop()
            if st:
                if not st[-1].left:
                    st[-1].left=nd
                else:
                    st[-1].right=nd
            st.append(nd)
        return st[0]