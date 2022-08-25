class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<String, Integer> countRN = new HashMap<>();
        HashMap<String, Integer> countM = new HashMap<>();
        for(String lett : ransomNote.split("")){
            if (countRN.containsKey(lett)){
                countRN.put(lett, countRN.get(lett)+1);
            }else{
                countRN.put(lett, 1);
            }
        }
        for(String lett: magazine.split("")){
            if (countM.containsKey(lett)){
                countM.put(lett, countM.get(lett)+1);
            }else{
                countM.put(lett, 1);
            }
        }
        for (String lett: ransomNote.split("")){
            if (!countM.containsKey(lett)){
                return false;
            }
            if (countRN.get(lett) > countM.get(lett)){
                return false;
            }
        }
        return true;
    }
}