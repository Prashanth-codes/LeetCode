class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2!=0:
            return []
        ans=[]
        s,t=2,0
        while s+t<=finalSum:
            ans.append(s)
            t+=s
            s+=2
        if t!=finalSum:
            ans[-1]+=(finalSum-t)
        return ans