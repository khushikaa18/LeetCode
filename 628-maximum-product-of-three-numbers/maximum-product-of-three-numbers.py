class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first=float('-inf')
        second=float('-inf')
        third=float('-inf')

        min1=min2=float('inf')

        for i in range(len(nums)):

            digit=nums[i]

            if digit>= first:
                third= second
                second=first
                first=digit
            elif digit>= second:
                third= second
                second= digit
            elif digit> third:
                third=digit
            
            if digit <= min1:
                min2= min1
                min1=digit
            elif digit < min2:
                min2=digit
            

        return max(first*second*third , first * min1 * min2)

