class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> ans =new ArrayList<>();
        backtrack(0,candidates,target,new ArrayList<>(),ans);
        return ans;
    }

    private void backtrack(int start,int[] candidates,int target,List<Integer>current,List<List<Integer>>ans){
        if(target==0){
            ans.add(new ArrayList<>(current));
            return;
        }

        for(int i=start;i<candidates.length;i++){
            if(candidates[i]>target){
                break;
            }
            current.add(candidates[i]);
            backtrack(i,candidates,target-candidates[i],current,ans);
            current.remove(current.size()-1);
        }
    }
}