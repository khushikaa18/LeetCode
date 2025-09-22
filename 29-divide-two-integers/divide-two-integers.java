class Solution {
    public int divide(int dividend, int divisor) {
        if(divisor==-1 && dividend==Integer.MIN_VALUE){
            return Integer.MAX_VALUE;
        }
        int quotient=dividend/divisor;
        return quotient;
        
    }
}