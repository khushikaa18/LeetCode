class Solution {
    public boolean reorderedPowerOf2(int n) {
        char[] digits=String.valueOf(n).toCharArray();
        Arrays.sort(digits);

        do{
            if(digits[0]=='0'){
                continue;
            }
            int num=Integer.parseInt(new String(digits));
            if(PowerOfTwo(num)){
                return true;
            }
        }
         while(nextPermutation(digits));
        
        return false;
    }

    private boolean PowerOfTwo(int n){
        return (n>0) &&((n&(n-1))==0);
    }

    private boolean nextPermutation(char[] arr){
        int i=arr.length-2;
        while(i>=0 && arr[i]>=arr[i+1]){
            i--;
        }
        if(i<0){
            return false;
        }
        int j=arr.length-1;
        while(arr[j]<=arr[i]){
            j--;
        }
        swap(arr,i,j);
        reverse(arr,i+1,arr.length-1);
        return true;
    }

    private void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    private void reverse(char[] arr, int i, int j) {
        while (i < j) swap(arr, i++, j--);
    }
}