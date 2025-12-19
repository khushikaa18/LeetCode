class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";

        int[] hash = new int[256];

        for (int i = 0; i < t.length(); i++) {
            hash[t.charAt(i)]++;
        }

        int l = 0, r = 0;
        int count = 0;
        int start = 0;
        int minLen = Integer.MAX_VALUE;

        while (r < s.length()) {
            if (hash[s.charAt(r)] > 0) {
                count++;
            }
            hash[s.charAt(r)]--;
            r++;

            while (count == t.length()) {
                if (r - l < minLen) {
                    minLen = r - l;
                    start = l;
                }

                hash[s.charAt(l)]++;
                if (hash[s.charAt(l)] > 0) {
                    count--;
                }
                l++;
            }
        }

        return minLen == Integer.MAX_VALUE ? "" : s.substring(start, start + minLen);
    }
}
