class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        List<List<Integer>> result = new ArrayList<>();
        int min_diff=Integer.MAX_VALUE;
        for(int i=0;i<arr.length-1;i++){
            int current_diff=arr[i+1]-arr[i];

            if(current_diff<min_diff){
                min_diff=current_diff;
                result.clear();
                result.add(Arrays.asList(arr[i],arr[i+1]));
            }
            else if ( current_diff==min_diff){
                result.add(Arrays.asList(arr[i],arr[i+1]));
            }
        }
        return result;
    }
}