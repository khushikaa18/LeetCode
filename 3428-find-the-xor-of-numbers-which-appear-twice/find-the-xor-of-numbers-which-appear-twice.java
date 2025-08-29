class Solution {
    public int duplicateNumbersXOR(int[] nums) {
        Arrays.sort(nums);
        int result=0;
        if(nums.length==0||nums.length==1){
            return 0;
        }
        for(int i=0;i<nums.length;i++){
            if(nums[i]==nums[(i+1)%nums.length]){
                result=result^nums[i];
                i++;
            }
        }
        return result;
    }
}