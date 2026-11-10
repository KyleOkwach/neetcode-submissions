impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut left: usize = 0;
        let mut right: usize = numbers.len().saturating_sub(1);

        let mut out: Vec<i32> = Vec::new();

        while right > left {
            let sum: i32 = numbers[left] + numbers[right];
            if sum == target {
                out.push((left + 1) as i32);
                out.push((right + 1) as i32);
                break
            } else if sum < target {
                left += 1;
            } else {
                right -= 1;
            }
        }

        out
    }
}
