class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        w1=Counter(ransomNote)
        w2=Counter(magazine)

        for ch in w1:
            if w1[ch]>w2[ch]:
                return False
        
        return True