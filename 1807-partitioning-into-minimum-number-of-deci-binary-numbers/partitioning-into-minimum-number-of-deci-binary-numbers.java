class Solution {
    public int minPartitions(String n) {
        int maxdigit=0;

        for(char ch : n.toCharArray()){
            int digit=ch-'0';
            maxdigit=Math.max(maxdigit,digit);

            if(maxdigit==9){
                break;
            }
        }
        return maxdigit;
    }
}