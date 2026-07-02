class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def can_make(gap):
            count=1
            last=price[0]

            for i in range(1,len(price)):
                if price[i]-last>=gap:
                    count+=1
                    last=price[i]
                
                if count==k:
                    return True
            
            return False
        
        low=0
        high=price[-1]-price[0]
        ans=0

        while high>=low:
            mid=(high+low)//2
            if can_make(mid):
                ans=mid
                low=mid+1
            
            else:
                high=mid-1
        
        return ans