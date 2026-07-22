class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        #count=0
        #for i in range (10**n):
         #   s=str(i)

          #  if len(s)==len(set(s)):
           #     count+=1
        #return count

        if n==0:
            return 1

        ans=10
        unique=9
        available=9

        while n>1 and available>0:
            unique *= available
            ans+=unique
            available-=1
            n-=1
        return ans 
