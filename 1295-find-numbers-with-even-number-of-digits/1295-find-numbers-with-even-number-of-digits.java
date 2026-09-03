class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (even(nums[i])%2 == 0){
                count ++;
            }
        }
        return count;
    }

    private int even(int num) {
        int digits = 0;
        while (num > 0){
            digits++;
            num = num/10;
        }
        return digits;
    }
}