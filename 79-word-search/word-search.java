class Solution {
    public boolean exist(char[][] board, String word) {
        int m=board.length,n=board[0].length;
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(word.charAt(0)==board[i][j])
                {
                    if(dfs(0,i,j,word,board,m,n))
                    return true;
                }
            }
        }
        return false;
    }
    int di[]={-1,0,1,0};
    int dj[]={0,1,0,-1};
    public boolean dfs(int idx,int i,int j,String w,char b[][],int m,int n)
    {
        if(w.length()==idx)
        return true;
        if(i<0 || i>=m || j<0 || j>=n || b[i][j]!=w.charAt(idx))
        return false;
        char temp=b[i][j];
        b[i][j]='#';
        for(int k=0;k<4;k++)
        {
            if(dfs(idx+1,i+di[k],j+dj[k],w,b,m,n))
            return true;
        }
        b[i][j]=temp;
        return false;
    }
}