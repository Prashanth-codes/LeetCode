class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        nums.sort()
        ans,c=1,1
        prev=nums[0]
        for i in range(1,n):
            if nums[i]==prev:
                continue
            elif nums[i]-1==prev:
                c+=1
            else:
                ans=max(ans,c)
                c=1
            prev=nums[i]
        ans=max(ans,c)
        return ans