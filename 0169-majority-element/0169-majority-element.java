class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer,Integer> m1 = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            m1.put(nums[i], m1.getOrDefault(nums[i], 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : m1.entrySet()) {
            if (entry.getValue() > nums.length/2) {
                return entry.getKey();
            }
        }

        return 0;
    }
}