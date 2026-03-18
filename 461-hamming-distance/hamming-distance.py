class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        if x==y:
            return 0
        n=x^y
        while n:
            n = n & (n-1)
            count+=1
        return count
