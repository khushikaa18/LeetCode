class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<>();
        
        if (nums.length == 0) return result;
        
        int start = nums[0]; // starting number of current range
        
        for (int i = 1; i <= nums.length; i++) {
            // break condition: end of array OR non-consecutive number
            if (i == nums.length || nums[i] != nums[i - 1] + 1) {
                int end = nums[i - 1]; // last number in current range
                
                if (start == end) {
                    result.add(String.valueOf(start)); // single number
                } else {
                    result.add(start + "->" + end); // range
                }
                
                // reset start for next range
                if (i < nums.length) {
                    start = nums[i];
                }
            }
        }
        
        return result;
    }
}
