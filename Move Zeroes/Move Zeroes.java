import java.util.ArrayList;

class Solution {
    public void moveZeroes(int[] nums) {
        ArrayList<Integer> arr = new ArrayList<Integer>();
        int countZero = 0;
        
        for (int i = 0; i < nums.length; i++){
            if (nums[i] != 0) {
                arr.add(nums[i]);
            }
            else {
                countZero++;
            }            
        }
        while (countZero > 0) {
            arr.add(0);
            countZero--;
        }
        Integer[] numsCopy = arr.toArray(new Integer[0]);
        for (int k = 0; k < nums.length; k++) {
            nums[k] = numsCopy[k];   
        }
    }
}
