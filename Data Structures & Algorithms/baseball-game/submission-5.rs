impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        let mut record = vec![];
        for (i, op) in operations.into_iter().enumerate() {
            if let Ok(r) = op.parse::<i32>() {
                record.push(r);
            } else if op == "D" {
                let r = record.pop().unwrap();
                record.push(r);
                record.push(r * 2);
            } else if op == "+" {
                let r2 = record.pop().unwrap();
                let r1 = record.pop().unwrap();
                record.push(r1);
                record.push(r2);
                record.push(r1+r2);
            } else if op == "C" {
                record.pop();
            }
        }
        record.into_iter().sum()
    }
}
