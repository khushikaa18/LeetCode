class Solution {
    public void nextPermutation(int[] nums) {
       int n = nums.length;
        int i = n - 2;

        // Step 1: Right side se pehla 'dip' (nums[i] < nums[i+1]) dhundhein
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        if (i >= 0) {
            // Step 2: i se just bada number right side se dhundhein
            int j = n - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            // Swap i and j
            swap(nums, i, j);
        }

        // Step 3: i ke baad wale portion ko reverse karein
        reverse(nums, i + 1, n - 1);
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        } 
    }
}