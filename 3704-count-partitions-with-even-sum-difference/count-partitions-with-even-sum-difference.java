class Solution {
    public int countPartitions(int[] nums) {
        int count=0;
        int sum=0;
        int n=nums.length;
        int leftsum=0;
        for(int i=0;i<n;i++){
            sum+=nums[i];
        }
        for(int i=0;i<n-1;i++){
            leftsum+=nums[i];
            int rightsum=sum-leftsum;

            if((leftsum-rightsum)%2==0){
                count++;
            }
        }
        return count;
    }
}