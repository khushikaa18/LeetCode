class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[-1]))

        count=0
        maxright=0

        for left,right in intervals:
            if right>maxright:
                count+=1
                maxright=right
        
        return count