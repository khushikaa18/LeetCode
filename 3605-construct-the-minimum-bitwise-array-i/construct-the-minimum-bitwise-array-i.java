class Solution {
    public int[] minBitwiseArray(List<Integer> nums) {
        int n = nums.size();
        int[] ans = new int[n];

        for (int i = 0; i < n; i++) {
            int val = nums.get(i);

            if ((val & 1) == 0) {   // even
                ans[i] = -1;
            } else {
                int temp = val;
                int count = 0;

                // count trailing 1s
                while ((temp & 1) == 1) {
                    count++;
                    temp >>= 1;
                }

                ans[i] = val - (1 << (count - 1));
            }
        }
        return ans;
    }
}

