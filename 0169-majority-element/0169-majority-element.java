class Solution {
    public int majorityElement(int[] nums) {
        //Moore Voting Algorithm
        int count = 0;
        int occur = 0;

        for (int num : nums) {
            if (count == 0) {
                occur = num;
            }

            if (num == occur) {
                count++;
            } else {
                count--;
            }
        }

        return occur;
    }
}