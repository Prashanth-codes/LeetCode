/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode recoverFromPreorder(String traversal) {
        Stack<TreeNode> st=new Stack<>();
        int i=0,n=traversal.length();
        while(i<n)
        {
            int d=0;
            while(i<n && traversal.charAt(i)=='-')
            {
                d+=1;
                i+=1;
            }
            String s="";
            while(i<n && Character.isDigit(traversal.charAt(i)))
            {
                s+=traversal.charAt(i);
                i+=1;
            }
            int num=Integer.parseInt(s);
            TreeNode nd=new TreeNode(num);
            while(st.size()>d)
            {
                st.pop();
            }
            if(!st.isEmpty())
            {
                if(st.peek().left==null)
                st.peek().left=nd;
                else
                st.peek().right=nd;
            }
            st.push(nd);
        }
        return st.get(0);
    }
}