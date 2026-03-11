class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a=format(n, 'b')
        inverse_s = ''.join(['1' if i == '0' else '0' for i in a])
        b=int(inverse_s,2)

        return b 