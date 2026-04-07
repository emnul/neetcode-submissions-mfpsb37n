impl Solution {
    pub fn replace_elements(arr: Vec<i32>) -> Vec<i32> {
        let n: usize = arr.len();
        let mut ans = arr.clone();
        let mut right_max = -1;
        for i in (0..n).rev() {
            ans[i] = right_max;
            right_max = right_max.max(arr[i]);
        }
        ans
    }
}
