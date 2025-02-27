class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n=len(arr)
        s=set(arr)
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                c=2
                prev=arr[j]
                temp=arr[i]+arr[j]
                while temp in s:
                    prev,temp=temp,temp+prev
                    c+=1
                if c!=2:
                    ans=max(ans,c)
        return ans