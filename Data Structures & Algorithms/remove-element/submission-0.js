class Solution {
    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
    removeElement(nums, val) {
        let k = nums.length;
        for (let i = 0; i < nums.length; ) {
            if (nums[i] === val) {
                nums.splice(i, 1);
                k--;
            } else if (nums[i] !== val) {
                i++;
            }
        }

        return k
    }
}
