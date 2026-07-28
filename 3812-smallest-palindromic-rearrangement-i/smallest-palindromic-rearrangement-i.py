class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        
        left=[]
        mid=""
        freq=Counter(s)

        for char in sorted(freq):
            left.append(char * (freq[char]//2))
            if freq[char] % 2 !=0:
                mid=char
        
        left="".join(left)
        return left+mid+left[::-1]