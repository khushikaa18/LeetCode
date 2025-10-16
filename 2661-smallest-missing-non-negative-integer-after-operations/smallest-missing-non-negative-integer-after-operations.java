class Solution {
    public int findSmallestInteger(int[] nums, int value) {
        Map<Integer,Integer> remCount=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int rem=(nums[i]%value+value)%value;
            remCount.put(rem,remCount.getOrDefault(rem,0)+1);
        }
        int mex=0;
        while(true){
            int rem=mex%value;
            if(remCount.getOrDefault(rem,0)>0){
                remCount.put(rem,remCount.get(rem)-1);
                mex++;
            }
            else{
                return mex;
            }
        }

    }
}