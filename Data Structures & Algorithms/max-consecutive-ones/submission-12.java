class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0;
        int streak = 0;

        for (int val : nums) {
            if (val == 1) {
                streak++;
            }
            else {
                if (streak > max) {
                    max = streak;
                }
                streak = 0;
            }
        }

        return (streak > max) ? streak : max;
    }
}