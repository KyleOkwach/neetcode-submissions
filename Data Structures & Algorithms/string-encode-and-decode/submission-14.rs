impl Solution {
    pub fn encode(strs: Vec<String>) -> String {
        let mut encoded: String = String::new();
        for s in strs {
            encoded.push_str(&format!("{}#{}", s.len(), s));
        }
        println!("{:?}", encoded);
        encoded
    }

    pub fn decode(s: String) -> Vec<String> {
        let mut decoded = Vec::new();
        let mut i = 0;
        let bytes = s.as_bytes();

        while i < bytes.len() {
            let mut j = i;
            while bytes[j] != b'#' {
                j += 1;
            }

            let len: usize = s[i..j].parse().unwrap();
            let start = j + 1;
            let end = start + len;
            decoded.push(s[start..end].to_string());

            i = end;
        }
        
        decoded
    }
}
