impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let chars: Vec<char> = s.chars().collect();
        let mut left: usize = 0;
        let mut right: usize = chars.len().saturating_sub(1);

        while right > left {
            // Check left
            while left < right && !chars[left].is_alphanumeric() {
                left += 1;
            }

            while right > left && !chars[right].is_alphanumeric() {
                right -= 1;
            }

            let left_char = chars[left].to_ascii_lowercase();
            let right_char = chars[right].to_ascii_lowercase();

            if left_char != right_char { return false; }


            left += 1;
            right = right.saturating_sub(1);
        }

        true
    }
}
