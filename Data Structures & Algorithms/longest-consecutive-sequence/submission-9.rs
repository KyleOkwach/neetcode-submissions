use std::collections::HashSet;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        // Store numbers in a HashSet for O(1) lookups and deduplication
        let num_set: HashSet<i32> = nums.into_iter().collect();
        let mut longest = 0;

        for &n in &num_set {
            // Only start counting if `n` is the beginning of a sequence
            if !num_set.contains(&(n - 1)) {
                let mut current_num = n;
                let mut current_streak = 1;

                while num_set.contains(&(current_num + 1)) {
                    current_num += 1;
                    current_streak += 1;
                }

                longest = longest.max(current_streak);
            }
        }

        longest
    }
}
