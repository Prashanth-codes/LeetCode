class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        b,e,a=[],[],[]
        for n in nums:
            if n<pivot:
                b.append(n)
            elif n==pivot:
                e.append(n)
            else:
                a.append(n)
        return b+e+a