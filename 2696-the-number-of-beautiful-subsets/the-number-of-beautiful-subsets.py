class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        c=0
        n=len(nums)
        def backtrack(idx,l):
            nonlocal c
            if l:
                c+=1
            for i in range(idx,n):
                flag=True
                for num in l:
                    if abs(num-nums[i])==k:
                        flag=False
                        break
                if flag:
                    l.append(nums[i])
                    backtrack(i+1,l)
                    l.pop()
        backtrack(0,[])
        return c
