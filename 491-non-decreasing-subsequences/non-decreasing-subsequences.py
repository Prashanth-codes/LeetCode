class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=set()
        def backtrack(idx,l):
            if len(l)>=2:
                ans.add(tuple(l))
            if idx==n:
                return
            for i in range(idx,n):
                if l:
                    if l[-1]<=nums[i]:
                        l.append(nums[i])
                        backtrack(i+1,l)
                        l.pop()
                else:
                    l.append(nums[i])
                    backtrack(i+1,l)
                    l.pop()
        backtrack(0,[])
        return list(map(list,ans))