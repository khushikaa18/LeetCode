class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_map={0:-1}
        curr_sum=0
        max_len=0

        for i in range(len(nums)):
            if nums[i]==0:
                curr_sum +=-1
            else:
                curr_sum+=1
            
            if curr_sum in prefix_map:
                max_len=max(max_len,i-prefix_map[curr_sum])
            
            else:
                prefix_map[curr_sum]=i
        
        return max_len
