class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mp=defaultdict(int)
        for a in nums1:
            mp[a[0]]+=a[1]
        for a in nums2:
            mp[a[0]]+=a[1]
        ans=[list(i) for i in sorted(mp.items())]
        return ans