class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        mx=0
        for w,v in boxTypes:
            if w<=truckSize:
                mx+=(w*v)
                truckSize-=w
            else:
                mx+=truckSize*v
                break
        return mx