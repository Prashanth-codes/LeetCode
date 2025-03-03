class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        c=[1]*n
        mx=1
        for i in range(n):
            for j in  range(i):
                if nums[j]<nums[i]:
                    if dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
                        c[i]=c[j]
                    elif dp[j]+1==dp[i]:
                        c[i]+=c[j]
            mx=max(mx,dp[i])
        cnt=0
        for i in range(n):
            if dp[i]==mx:
                cnt+=c[i]
        return cnt