impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut counts = [0; 26];

        for (s_byte, t_byte) in s.bytes().zip(t.bytes()) {
            counts[(s_byte - b'a') as usize] += 1;
            counts[(t_byte - b'a') as usize] -= 1;
        }

        counts.iter().all(|&count| count == 0)
    }
}
