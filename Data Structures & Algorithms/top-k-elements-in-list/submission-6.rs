impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut freq: HashMap<i32, i32> = HashMap::new();

        for i in nums {
            *freq.entry(i).or_insert(0) += 1;
        }

        let mut freq_vec: Vec<(i32, i32)> = freq.into_iter().collect();
        freq_vec.sort_unstable_by(|a, b| b.1.cmp(&a.1));

        freq_vec
            .into_iter()
            .take(k as usize)
            .map(|(num, count)| num)
            .collect()
    }
}
