class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s,t=0,sum(nums)
        for i,n in enumerate(nums):
            if s==t-s-n:
                return i
            s+=n
        return -1