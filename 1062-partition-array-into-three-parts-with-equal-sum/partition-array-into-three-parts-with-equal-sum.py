class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n=len(arr)
        sm=sum(arr)
        if sm%3!=0:
            return False
        t=sm//3
        s,c=0,0
        for i in range(n-1):
            s+=arr[i]
            if s==t:
                c+=1
                s=0
                if c==2:
                    return True
        return False