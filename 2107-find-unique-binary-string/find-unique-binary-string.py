class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        ans=""
        for i in range(n):
            ans+='0' if nums[i][i]=='1' else '1'
        return ans