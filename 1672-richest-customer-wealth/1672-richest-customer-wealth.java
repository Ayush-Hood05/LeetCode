class Solution {
    public int maximumWealth(int[][] accounts) {
        int max_sum = Integer.MIN_VALUE;
        for (int i = 0; i < accounts.length; i++) {
            int total = 0;
            for (int j = 0; j < accounts[i].length; j++) {
                total += accounts[i][j];
            }
            max_sum = Math.max(total,max_sum);
        }
        return max_sum;
    }
}