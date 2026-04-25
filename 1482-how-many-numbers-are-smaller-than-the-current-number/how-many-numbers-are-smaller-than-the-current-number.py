class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """
        ans=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if j!=i and nums[j]<nums[i]:
                    count+=1
            ans.append(count)
        return ans
        """
        sorted_num=sorted(nums)
        rank={}

        for i,num in enumerate(sorted_num):
            if num not in rank:
                rank[num]=i
        
        return [rank[num] for num in nums]