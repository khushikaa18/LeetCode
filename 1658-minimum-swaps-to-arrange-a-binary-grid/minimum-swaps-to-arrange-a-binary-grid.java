class Solution {
    public int minSwaps(int[][] grid) {
        int n=grid.length;
        int [] trailingzeros=new int[n];

        for(int i=0;i<n;i++){
            int count=0;
            for(int j=n-1;j>=0 && grid[i][j]==0; j--){

                count++;
            }
            trailingzeros[i]=count;
        }
        int swaps=0;

        for(int i=0;i<n;i++){
            int required=n-1-i;
            int j=i;

            while(j<n && trailingzeros[j]<required){
                j++;
            }
            if(j==n){
                return -1;
            }

            while(j>i){
                int temp=trailingzeros[j];
                trailingzeros[j]=trailingzeros[j-1];
                trailingzeros[j-1]=temp;
                swaps++;
                j--;
            }
        }
        return swaps;
    }
}