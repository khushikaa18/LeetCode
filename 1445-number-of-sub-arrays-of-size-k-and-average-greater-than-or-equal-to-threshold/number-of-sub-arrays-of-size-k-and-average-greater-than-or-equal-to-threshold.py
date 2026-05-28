class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum=sum(arr[:k])
        best=0

        if window_sum/k>=threshold:
            best+=1


        for i in range(k,len(arr)):
            window_sum+=arr[i]-arr[i-k]
            
            if window_sum/k>=threshold:
                best+=1
        
        return best
