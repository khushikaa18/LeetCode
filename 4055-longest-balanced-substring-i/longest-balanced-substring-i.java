class Solution {
    public int longestBalanced(String s) {
        int maxLen = 0;
        for (int i = 0; i < s.length(); i++) {
            int[] count = new int[26]; 
            int distinctCount = 0;

            for (int j = i; j < s.length(); j++) {
                int charIdx = s.charAt(j) - 'a';
                if (count[charIdx] == 0) {
                    distinctCount++;
                }
                count[charIdx]++;

                int totalLen = j - i + 1;

                if (totalLen % distinctCount == 0) {
                    int target=totalLen/distinctCount;
                    boolean isBalanced = true;
                    for (int k = 0; k < 26; k++) {
                        if (count[k] > 0 && count[k] != target) {
                            isBalanced = false;
                            break; 
                        }
                    }

                    if (isBalanced) {
                        maxLen = Math.max(maxLen, totalLen);
                    }
                }
            }
        }
        return maxLen;
    }
}
