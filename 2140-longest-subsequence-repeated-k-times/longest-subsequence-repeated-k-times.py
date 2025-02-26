class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def help(ss,s):
            m,n=len(ss),len(s)
            i,j=0,0
            while i<m and j<n:
                if ss[i]==s[j]:
                    i+=1
                j+=1
            return i==m
        mp=defaultdict(lambda: 0)
        for c in s:
            mp[c]+=1
        f=[v for v in mp if mp[v]>=k]
        f.sort()
        ans=""
        st=[""]
        while st:
            pre=st.pop(0)
            for ch in f:
                ss=pre+ch
                if help(ss*k,s):
                    st.append(ss)
                    ans=ss
        return ans