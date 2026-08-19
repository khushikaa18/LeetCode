class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0

        bin_no=bin(n)[2:]

        for num in bin_no:
            if num =="1":
                count+=1
        
        return count 
        