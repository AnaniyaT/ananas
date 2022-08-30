class Solution {
    public void rotate(int[][] matrix) {
        int[][]copy = new int[matrix.length][matrix.length];
        for (int i = 0; i < matrix.length; i++){
            for (int j = 0; j < matrix.length ; j++){
                copy[i][j] = matrix[i][j];
            }
        }
        for (int i = 0; i < matrix.length; i++){
            int n =0;
            for (int j = matrix.length - 1; j >= 0; j--){
                matrix[i][n] = copy[j][i];
                n += 1;
            }
        }
    }
}