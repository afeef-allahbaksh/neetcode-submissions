class Solution {
    public int[] replaceElements(int[] arr) {
        // Go from the end of the list to the start
        int i = arr.length - 1;
        int largest_seen = arr[i];
        arr[i--] = -1;

        while (i >= 0) {
            int curr_val = arr[i];
            arr[i--] = largest_seen;

            if (curr_val > largest_seen) {
                largest_seen = curr_val;
            }
        }

        return arr;
    }
}