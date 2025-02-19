class Solution {
    public String getHappyString(int n, int k) {
        String arr[]={"a","b","c"};
        List<String> ans=new ArrayList<>();
        List<String> l=new ArrayList<>();
        backtrack(n,l,ans,arr);
        if(ans.size()<k)
        return "";
        return ans.get(k-1);
    }
    public void backtrack(int n,List<String> l,List<String> ans,String arr[])
    {
        if(l.size()==n)
        {
            String s="";
            for(int i=0;i<n;i++)
            s+=l.get(i);
            ans.add(s);
            return;
        }
        for(String s:arr)
        {
            if(l.size()==0)
            {
                l.add(s);
                backtrack(n,l,ans,arr);
                l.remove(l.size()-1);
            }
            else
            {
                if(!l.get(l.size()-1).equals(s))
                {
                    l.add(s);
                    backtrack(n,l,ans,arr);
                    l.remove(l.size()-1);
                }
            }
        }
    }
}