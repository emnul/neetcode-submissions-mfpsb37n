impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let mut ans = nums.clone();
        for item in nums {
            ans.push(item);
        }
        ans
    }
}
