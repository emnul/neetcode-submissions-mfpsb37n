impl Solution {
    pub fn replace_elements(arr: Vec<i32>) -> Vec<i32> {
        let mut ret = arr.clone();
        let len = ret.len();
        let mut tmp = ret[len - 1];
        ret[len - 1] = -1;
        for i in (0..len - 1).rev() {
            let max = if tmp > ret[i+1] {
                tmp
            } else {
                ret[i + 1]
            };
            tmp = ret[i];
            ret[i] = max;
        }
        ret
    }
}
