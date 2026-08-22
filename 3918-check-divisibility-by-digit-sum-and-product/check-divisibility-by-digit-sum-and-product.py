class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = sum(int(d) for d in str(n))

        digit_prod=1

        for d in str(n):
            digit_prod*=int(d)
        
        total=digit_sum + digit_prod
        return n % total==0