struct MinStack {
    internal: Vec<i32>,
    // The key insight here is to use another stack to track
    // the min value as the stack grows / shrinks
    min_stack: Vec<i32>
}

impl MinStack {
    pub fn new() -> Self {
        Self {
            internal: vec![],
            min_stack: vec![],
        }
    }

    pub fn push(&mut self, val: i32) {
        // if stack is empty return max value else last value is current min
        let current_min = *self.min_stack.last().unwrap_or(&i32::MAX);
        if val <= current_min {
            // update current min by pushing val to top of min_stack
            self.min_stack.push(val);
        } else {
            // else push current min to top
            self.min_stack.push(current_min);
        }
        self.internal.push(val);
    }

    pub fn pop(&mut self) {
        // make sure to update both stacks
        self.min_stack.pop();
        self.internal.pop();
    }

    pub fn top(&self) -> i32 {
        let len = self.internal.len();
        self.internal[len - 1]
    }

    pub fn get_min(&self) -> i32 {
        // last returns a Option<&T> so we need to unwrap it and deref
        *self.min_stack.last().unwrap()
    }
}

