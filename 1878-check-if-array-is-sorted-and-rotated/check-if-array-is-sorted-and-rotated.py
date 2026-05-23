class Solution:
    def check(self, nums: List[int]) -> bool:
        rotationPoint=0

        for  i in range(len(nums)):
            if nums[i]>nums[(i+1)%len(nums)]:
                rotationPoint+=1
                continue
        
        if  rotationPoint>1:
            return False
        else:
            return True
            