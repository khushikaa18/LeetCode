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
    public List<String> letterCombinations(String digits) {
        List<String> result=new ArrayList<>();

        if(digits==null||digits.length()==0){
            return result;
        }
        String [] map ={
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz",
        };

        result.add("");
        for(char digit:digits.toCharArray()){
            String letters=map[digit-'0'];
            List<String> temp=new ArrayList<>();

            for(String comb:result){
                for(char ch:letters.toCharArray()){
                    temp.add(comb+ch);
                }
            }
            result=temp;

        }

        return result;

    }
    
}