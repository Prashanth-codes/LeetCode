class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        def backtrack(s,c):
            nonlocal ans
            ans+=c
            if s==n:
                return
            for i in range(s,n):
                c^=nums[i]
                backtrack(i+1,c)
                c^=nums[i]
        backtrack(0,0)
        return ans