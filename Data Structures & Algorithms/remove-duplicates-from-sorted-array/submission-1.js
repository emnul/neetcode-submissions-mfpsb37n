class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        let ndx = 0;
        let k = 0;
        for (let i = 0; i < nums.length; ) {
            if (nums[i] === nums[ndx] && i === ndx) {
                k++;
                i++;
            } else if (nums[i] === nums[ndx] && i !== ndx) {
                nums.splice(i, 1);
            } else if (nums[i] !== nums[ndx]) {
                i++;
                ndx++;
                k++;
            }
            
        }
        return k;
    }
}
