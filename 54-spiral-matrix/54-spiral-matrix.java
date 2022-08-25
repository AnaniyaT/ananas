class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int m = 0;
        int n = 0;
        String d = "r";
        int[] limit = {matrix[0].length-1, 0, 1, matrix.length-1};
        List<Integer> list = new ArrayList<>();
        
        for (int i = 0; i < (matrix[0].length*matrix.length); i++){
            list.add(matrix[m][n]);
            if(d == "r"){
                if(n==limit[0]){
                    d = "d";
                    limit[0] -= 1;
                    m += 1;
                }else{
                    n += 1;
                }
                
            }else if(d == "l"){
                if (n == limit[1]){
                    d = "u";
                    limit[1] += 1;
                    m -= 1;
                }else{
                    n -= 1;
                }
                
            }else if (d == "d"){
                if (m == limit[3]){
                    d = "l";
                    limit[3] -= 1;
                    n -= 1;
                }else{
                    m += 1;
                }
                
            }else if(d == "u"){
                if (m == limit[2]){
                    d = "r";
                    limit[2] += 1;
                    n += 1;
                }else{
                    m -= 1;
                }
            }
        }
        return list;
    }
}   