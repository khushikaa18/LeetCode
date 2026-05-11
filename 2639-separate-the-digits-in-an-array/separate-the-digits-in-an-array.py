class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        digits = [int(digit) for num in nums for digit in str(num)]
        return digits

