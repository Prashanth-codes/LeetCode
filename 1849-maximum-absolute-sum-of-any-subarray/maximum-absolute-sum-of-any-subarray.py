class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans,temp=0,0
        for i in nums:
            if i>temp+i:
                temp=i
            else:
                temp+=i
            ans=max(ans,temp)
        temp=0
        for i in nums:
            if i<temp+i:
                temp=i
            else:
                temp+=i
            ans=max(ans,abs(temp))
        return ans