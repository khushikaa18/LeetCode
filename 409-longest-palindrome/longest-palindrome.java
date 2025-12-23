class Solution {
    public int longestPalindrome(String s) {
        int[] freq = new int[128]; // ASCII characters
        
        // Step 1: Frequency count
        for (char ch : s.toCharArray()) {
            freq[ch]++;
        }
        
        int length = 0;
        boolean hasOdd = false;
        
        // Step 2: Build palindrome length
        for (int count : freq) {
            if (count % 2 == 0) {
                length += count;
            } else {
                length += count - 1;
                hasOdd = true;
            }
        }
        
        // Step 3: One odd character can be placed in center
        if (hasOdd) length++;
        
        return length;
    }
}
