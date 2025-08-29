class Solution {
    public boolean check(int[] nums) {
        int rotationpoint=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]>nums[(i+1)%nums.length]){
                rotationpoint++;
                if(rotationpoint>1){
                    return false;
                }
            }
        }
        return true;
    }
}