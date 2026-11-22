impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut store: HashMap<[u32; 26], Vec<String>> = HashMap::new();

        for string in strs {
            let key = Self::get_bytes(&string);
            
            store.entry(key).or_insert_with(Vec::new).push(string);
        }

        store.into_values().collect()
    }

    pub fn get_bytes(text: &str) -> [u32; 26] {
        let mut counts = [0; 26];

        for text_byte in text.bytes() {
            counts[(text_byte - b'a') as usize] += 1;
        }
        counts
    }
}