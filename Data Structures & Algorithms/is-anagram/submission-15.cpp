class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        std::vector<uint32_t> count(26, 0);

        for(uint32_t i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }

        for (uint32_t val: count) {
            if (val != 0) {
                return false;
            }
        }

        return true;
    }
};
