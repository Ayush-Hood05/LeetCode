class Solution {
    public int maxSubArray(int[] nums) {
        int ptr_sum = 0;
        int max_val = Integer.MIN_VALUE;

        for (int i = 0; i < nums.length; i++) {
            ptr_sum += nums[i];
            max_val = Integer.max(max_val,ptr_sum);
            
            if (ptr_sum < 0){
                ptr_sum = 0;
            }
        }
        return max_val;
    }
}