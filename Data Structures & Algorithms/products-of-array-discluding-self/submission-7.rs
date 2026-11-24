impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut pre: Vec<i32> = vec![0; nums.len()];
        let mut post: Vec<i32> = vec![0; nums.len()];
        let mut curr: i32 = 1;
        let mut i = 0;

        // Populate prefix vector
        while i < nums.len() {
            pre[i] = curr;
            curr *= nums[i];
            i += 1;
        }

        curr = 1;
        i -= 1;
        while i > 0 {
            post[i] = curr;
            curr *= nums[i];
            i -= 1;
        }
        post[0] = curr;

        pre.iter()
            .zip(&post)
            .map(|(x, y)| x * y)
            .collect()
    }
}
