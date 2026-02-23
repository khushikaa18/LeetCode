
class Solution {
    public int maxArea(int[] height) {
        int i=0;
        int j=height.length-1;
        int maxArea=0;
        while(i<j){
            int Area=Math.min(height[i],height[j])*(j-i);
            maxArea=Math.max(maxArea,Area);
            if(height[i]<height[j] || height[i]==height[j]){
            i++;
            }
            else{
                j--;
            } 
            
        }
        return maxArea;
    }
}