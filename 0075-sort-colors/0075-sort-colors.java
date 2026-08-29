class Solution {
    public void sortColors(int[] nums) {
        int start = 0 , end = nums.length-1 , ptr = 0;
        while (ptr <= end){
            if (nums[ptr] == 0){
                int temp = nums[start];
                nums[start] = nums[ptr];
                nums[ptr] = temp;
                start++;
                ptr++;
            }
            else if (nums[ptr] == 1){
                ptr++;
            }
            else{
                int temp = nums[end];
                nums[end] = nums[ptr];
                nums[ptr] = temp;
                end --;
            }
        }
    }
}