class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
for (int num : nums1) {
    set1.add(num);
}
// Same for set2
        Set<Integer> set2= new HashSet<>();
        for(int num:nums2){
            set2.add(num);
        }
        Set<Integer> Intersection= new HashSet<>(set1);

        Intersection.retainAll(set2);
        int[] result=new int[Intersection.size()];
        int i=0;
        for( int num:Intersection){
            result[i++]=num;
        }


        return result;
    }
}