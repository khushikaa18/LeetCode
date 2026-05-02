class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> r = new ArrayList<>();
        for(int i=1;i<10;++i){
          recur(i, n, r); 
        }
        return r;
    }
    
    public void recur(int ans, int n, List<Integer> r){
        if(ans>n){
            return;
        }
        else{
            r.add(ans);
            for(int i=0;i<10;++i){
                if(10*ans+i>n){
                    return;
                }
                recur(10*ans+i, n, r);   
            }
        }
    }
}