class Solution {
    public int findDuplicate(int[] nums) {
        /*Arrays.sort(nums);
        for(int i=1;i<nums.length;i++){
           if(nums[i]==nums[i-1]){
            return nums[i];
           }
        }
        return 0;*/
        //Floyd warshall cycle hare and tortoise method
        int slow=nums[0];
        int fast=nums[0];
        do{
            slow=nums[slow];
            fast=nums[nums[fast]];

        }while(slow!=fast);
        slow=nums[0];

        while(slow!=fast){
            slow=nums[slow];
            fast=nums[fast];
        }
        return fast;
    }
}