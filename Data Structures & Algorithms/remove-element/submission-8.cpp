class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int curr = 0;
        int look_ahead = 0;

        while (look_ahead < nums.size()) {
            if (nums[look_ahead] != val) {
                nums[curr] = nums[look_ahead];
                curr++;
            }
            look_ahead++;
        }

        return curr;
    }
};