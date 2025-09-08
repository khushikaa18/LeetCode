class Solution {
    public int singleNumber(int[] nums) {
        int index=0,index1=0;
        for(int i=0;i<nums.length;i++){
            index=(index^nums[i])&~index1;
            index1=(index1^nums[i])&~index;
        }
        return index;
        
    }
}