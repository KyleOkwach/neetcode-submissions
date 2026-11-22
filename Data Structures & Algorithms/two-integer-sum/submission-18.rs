impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut store = HashMap::new();

        for (i, &n) in nums.iter().enumerate() {
            let complement = target - n;

            // If Some gets a value, the complement exists
            // else the step is skipped
            if let Some(&complement_idx) = store.get(&complement) {
                return vec![complement_idx, i as i32];
            }

            store.insert(n, i as i32);
        }

        vec![]
    }
}
