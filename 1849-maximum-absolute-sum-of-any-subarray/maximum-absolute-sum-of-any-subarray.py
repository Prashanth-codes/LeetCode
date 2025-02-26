class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        p=[0]
        for i in nums:
            p.append(p[-1]+i)
        return max(p)-min(p)