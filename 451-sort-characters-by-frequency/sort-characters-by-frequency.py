class Solution:
    def frequencySort(self, s: str) -> str:
        string=Counter(s)

        sorted_chars = sorted(
            string,
            key=lambda ch: string[ch],
            reverse=True
        )

        result = ""

        for ch in sorted_chars:
            result += ch * string[ch]

        return result
        