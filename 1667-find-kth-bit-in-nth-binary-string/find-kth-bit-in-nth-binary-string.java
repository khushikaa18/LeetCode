class Solution {
    public char findKthBit(int n, int k) {
        if(n==1) return '0';

        int L= (1<<n)-1;
        int mid= 1<< (n-1);

        if(k==mid){
            return '1';
        }
        if(k<mid){
            return findKthBit(n-1,k);
        }
        char bit= findKthBit(n-1,L-k+1);
        return bit == '0' ? '1' :'0';
    }
}