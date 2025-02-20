class Solution {
    public int minDistance(String word1, String word2) {
        int m=word1.length(),n=word2.length();
        int dp[][]=new int[m][n];
        for(int i=0;i<m;i++)
        Arrays.fill(dp[i],-1);
        return mindist(word1,word2,0,0,m,n,dp);
    }
    public int mindist(String a,String b,int i,int j,int m,int n,int dp[][])
    {
        if(i>=m)
        return n-j;
        if(j>=n)
        return m-i;
        if(dp[i][j]!=-1)
        return dp[i][j];
        if(a.charAt(i)==b.charAt(j))
        return mindist(a,b,i+1,j+1,m,n,dp);
        int ins=1+mindist(a,b,i,j+1,m,n,dp);
        int rem=1+mindist(a,b,i+1,j,m,n,dp);
        int rep=1+mindist(a,b,i+1,j+1,m,n,dp);
        return dp[i][j]=Math.min(ins,Math.min(rem,rep));
    } 
}