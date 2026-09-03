class Solution {
    public void nextPermutation(int[] nums) {
        // brute force will be the recursion find all solution and the linear search on all this greater just the i/p
        // optimal finding the pivot take a example as {1,2,3,6,5,4} -- {1 2 3(Pivot) < 6 > 5 > 4} 
        // swap 3 with the larger number that is 4 {1 2 4 |6 5 3|} -- | reverse this part | -- {1 2 4 3 5 6}

        // find the pivot 
        int pivot = -1 ;
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] < nums[i+1]){
                pivot = i;
                break;
            }
        }

        // pivot is not find the number its is largest make it smallest
        if (pivot == -1){
            int start = 0;
            int end = nums.length - 1;
            while (start < end){
                swap(nums, start, end);
                start ++;
                end --;
            }
            return;
        }
        
        // change the pivot with greater number
        if (pivot != -1){
            for (int i = nums.length-1; i > pivot; i--) {
                if (nums[i] > nums[pivot]){
                    swap(nums, pivot, i);
                    break;
                }
            }
        }

        // reverse 
        reverse(nums, pivot+1, nums.length-1);
    }

    public void swap (int nums[] , int i , int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public void reverse (int [] nums , int start , int end){
        // two pointer
        while (start < end){
            swap(nums,start,end);
            start ++;
            end --;
        }
    }

}