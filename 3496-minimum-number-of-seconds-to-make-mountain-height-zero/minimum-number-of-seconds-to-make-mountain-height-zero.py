class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def finish(time):
            total=0

            for w in workerTimes:
                k=time//w
                x=int((math.sqrt(1+8*k)-1)//2)
                total+=x

                if total>=mountainHeight:
                    return True
            return False

        
        left=1
        right=max(workerTimes)*mountainHeight*(mountainHeight+1)//2

        while left<right:
            mid=(left+right)//2

            if finish(mid):
                right=mid
            else:
                left=mid+1
        return left