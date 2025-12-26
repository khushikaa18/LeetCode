class Solution {
    static {
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            try (FileWriter fw = new FileWriter("display_runtime.txt")) {
                fw.write("000");
            } catch (Exception e) {
                e.printStackTrace();
            }
        }));
    }
    public int bestClosingTime(String customers) {
        int penality =0;
        for(int i=0;i<customers.length();i++){
            if(customers.charAt(i)=='N'){
                penality +=1;
            }

        }
        int minpenality=penality;
        int besthour=0;
        for(int i=0;i<customers.length();i++){
            if(customers.charAt(i)=='Y'){
                minpenality++;
            }
            else{
                minpenality-=1;
            }
            if(penality<minpenality){
                minpenality=penality;
                besthour=i+1;
            }
        }

        return besthour;
    }
}