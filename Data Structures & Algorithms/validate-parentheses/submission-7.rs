impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = vec![];
        for c in s.chars() {
            if c == '(' || c == '[' || c == '{' {
                stack.push(c);
            } else {
                // return false if brackets dont match
                if let Some(b) = stack.pop() {
                    if c == ')' && b != '(' {
                        return false;
                    } else if c == ']' && b != '[' {
                        return false;
                    } else if c == '}' && b != '{' {
                        return false;
                    }
                // if stack is exhausted before loop through s is complete
                // there are more left facing brackets than right ones
                } else {
                    return false;
                }
            }
        }
        // if stack is not exhausted after looping through s there are more 
        // right facing brackets than left
        if !stack.is_empty() {
            return false;
        }
        true
    }
}
