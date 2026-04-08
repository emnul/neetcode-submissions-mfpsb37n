struct MinStack {
    internal: Vec<i32>,
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
        let current_min = *self.min_stack.last().unwrap_or(&i32::MAX);
        if val <= current_min {
            self.min_stack.push(val);
        } else {
            self.min_stack.push(current_min);
        }
        self.internal.push(val);
    }

    pub fn pop(&mut self) {
        self.min_stack.pop();
        self.internal.pop();
    }

    pub fn top(&self) -> i32 {
        let len = self.internal.len();
        self.internal[len - 1]
    }

    pub fn get_min(&self) -> i32 {
        *self.min_stack.last().unwrap()
    }
}

