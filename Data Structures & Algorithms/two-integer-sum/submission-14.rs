impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut store = HashMap::new();

        for (i, n) in nums.iter().enumerate() {
            let complement: i32 = target - n;
            
            if store.contains_key(&complement) {
                // Complement exists
                let complement_idx = *store.get(&complement).unwrap();
                return vec![complement_idx, i as i32];
            }

            // Add to hashmap
            store.insert(n, i as i32);
        }

        vec![]
    }
}
