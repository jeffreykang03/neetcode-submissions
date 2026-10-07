class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> sc, tc;
        for(char c: s) sc[c]++;
        for(char c: t) tc[c]++;

        return sc == tc;

    }
};
