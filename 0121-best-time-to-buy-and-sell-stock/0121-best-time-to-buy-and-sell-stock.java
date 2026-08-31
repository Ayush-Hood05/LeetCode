class Solution {
    public int maxProfit(int[] prices) {
       // Kadane's rule
        int profit = 0;
        int buy = Integer.MAX_VALUE;

        for (int i = 0; i < prices.length; i++) {
            if (buy > prices[i]){
                buy = prices[i];
            } else if (prices[i]-buy > profit) {
                profit = prices[i]-buy;
            }
        }
        return profit;
    }
}