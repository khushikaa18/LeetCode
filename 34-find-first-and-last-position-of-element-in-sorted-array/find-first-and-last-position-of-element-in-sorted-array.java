class Solution {
    public int[] searchRange(int[] nums, int target) {
        int first=isBound(nums,target,true);
        int last=isBound(nums,target,false);
        return new int[]{first,last};
    }
        private int isBound(int[] nums,int target,boolean isfirst){
        int left=0,right=nums.length-1,ans=-1;
        while(left<=right){
            int mid=left+(right-left)/2;
            if(nums[mid]==target){
                ans=mid;
                if(isfirst){
                    right=mid-1;
                }
                else{
                    left=mid+1;
                }
            }
            else if(nums[mid]<target){
                left=mid+1;
            }
            else{
                right=mid-1;
            }
        }
        return ans;
    }
}