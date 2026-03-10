class Solution:
    def findMin(self, nums: List[int]) -> int:
        right=len(nums)-1
        left=0

        while(left<=right):
            mid=left+(right-left)//2

            if nums[mid] >nums[right]:
                left=mid+1
            elif nums[mid]<nums[right]:
                right=mid
            elif nums[mid]==nums[right]:
                right-=1
        
        return nums[left]