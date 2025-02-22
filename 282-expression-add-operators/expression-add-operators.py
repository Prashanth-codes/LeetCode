class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans=set()
        n=len(num)
        def backtrack(s,idx,v,l):
            if idx==n:
                if v==target:
                    ans.add(s)
                return
            for i in range(idx,n):
                temp=num[idx:i+1]
                no=int(temp)
                if len(temp)>1 and temp[0]=='0':
                    break
                if idx==0:
                    backtrack(temp,i+1,no,no)
                else:
                    backtrack(s+"+"+temp,i+1,v+no,no)
                    backtrack(s+"-"+temp,i+1,v-no,-no)
                    backtrack(s+"*"+temp,i+1,v-l+(l*no),l*no)
        backtrack("",0,0,0)
        return list(ans)