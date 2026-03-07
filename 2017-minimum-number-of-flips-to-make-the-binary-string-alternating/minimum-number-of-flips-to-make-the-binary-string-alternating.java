class Solution {
    public int minFlips(String s) {
        int n =s.length();
        s=s+s;
        int pattern1=0;
        int pattern2=0;
        int ans=Integer.MAX_VALUE;

        for(int i=0;i<s.length();i++){
            char expected1=(i%2==0)?'0':'1';
            char expected2=(i%2==0)?'1':'0';
            if(s.charAt(i)!=expected1){
                pattern1++;
            }
            if(s.charAt(i)!=expected2){
                pattern2++;
            }
            if(i>=n){
                char prev1=((i-n)%2==0)?'0':'1';
                char prev2=((i-n)%2==0)?'1':'0';

                if(s.charAt(i-n)!=prev1){
                    pattern1--;
                }
                if(s.charAt(i-n)!=prev2){
                    pattern2--;
                }
            }
            if(i>=(n-1)){
                ans=Math.min(ans,Math.min(pattern1,pattern2));
            }
        }
        return ans;
    }
}