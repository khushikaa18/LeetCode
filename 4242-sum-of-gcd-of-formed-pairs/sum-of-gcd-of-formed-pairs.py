class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefix_gcd=list()
        maxi=nums[0]

        for i in range(len(nums)):
            maxi=max(nums[i],maxi)
            prefix_gcd.append(gcd(nums[i],maxi))
        prefix_gcd.sort()

        left=0
        right=len(nums)-1
        ans=0

        while left<right:
            ans+=gcd(prefix_gcd[left],prefix_gcd[right])
            left+=1
            right-=1
        return ans