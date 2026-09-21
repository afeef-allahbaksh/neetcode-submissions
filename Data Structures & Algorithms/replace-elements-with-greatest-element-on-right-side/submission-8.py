class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        for i in range(len(arr)- 1, -1, -1):
            cur_val = arr[i]
            arr[i] = largest
            if (cur_val > largest):
                largest = cur_val
        
        return arr
        