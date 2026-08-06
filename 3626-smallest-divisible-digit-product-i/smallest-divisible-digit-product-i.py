class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while n !=0:
            number=n
            product=1

            while number>0:
                product *= number %10
                number//=10
            
            if product % t==0:
                return n 
            
            n+=1