class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = "".join(ch for ch in str(n) if ch != "0")

        if s == "":
            x = 0
        else:
            x = int(s)
        sum_digit=0

        for digit in str(n):
            sum_digit+=int(digit)
        
        return x * sum_digit
