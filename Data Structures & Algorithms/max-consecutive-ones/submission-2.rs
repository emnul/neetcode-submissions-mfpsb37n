impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut max = 0;
        let mut tmp = 0;
        for num in nums {
            if num == 1 {
                tmp += 1;
            } else {
                if max < tmp {
                    max = tmp;
                }
                tmp = 0;
            }
        }
        if max > tmp {
            max
        } else {
            tmp
        }
    }
}
