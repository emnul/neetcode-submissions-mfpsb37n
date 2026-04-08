impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = vec![];
        for c in s.chars() {
            if c == '(' || c == '[' || c == '{' {
                stack.push(c);
            } else {
                if let Some(b) = stack.pop() {
                    if c == ')' && b != '(' {
                        return false;
                    } else if c == ']' && b != '[' {
                        return false;
                    } else if c == '}' && b != '{' {
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }
        if !stack.is_empty() {
            return false;
        }
        true
    }
}
