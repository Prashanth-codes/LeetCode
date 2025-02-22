class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n,c=len(s),0
        st=[]
        for i in s:
            if i=="(":
                st.append(i)
            elif i==")":
                if not st:
                    c+=1
                if st and st[-1]=="(":
                    st.pop()
                if st and st[-1]!="(":
                    c+=1
                    st.pop()
        c+=len(st)
        ans=set()
        def backtrack(i,p,b,d):
            if b<0 or d>c:
                return
            if i==n:
                if b==0:
                    ans.add(p)
            if i<n and s[i]!="(" and s[i]!=")":
                backtrack(i+1,p+s[i],b,d)
            if i<n and s[i]=="(":
                backtrack(i+1,p+s[i],b+1,d)
                backtrack(i+1,p,b,d+1)
            if i<n and s[i]==")":
                backtrack(i+1,p+s[i],b-1,d)
                backtrack(i+1,p,b,d+1)
        backtrack(0,"",0,0)
        return list(ans)