class Solution:
    def mirrorDistance(self, n: int) -> int:
        reverse = int(str(n)[::-1])

        distance=abs(n-reverse)
        return distance