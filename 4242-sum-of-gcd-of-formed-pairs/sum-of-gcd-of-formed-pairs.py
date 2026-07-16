class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd=list()
        mxi=nums[0]

        for i in range(len(nums)):
            mxi=max(mxi,nums[i])
            prefixGcd.append(gcd(nums[i],mxi))
        prefixGcd.sort()

        left=0
        right=len(nums)-1
        ans=0

        while left < right:
            ans+=gcd(prefixGcd[left],prefixGcd[right])
            left+=1
            right-=1
        return ans
            