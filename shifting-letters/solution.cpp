class Solution {
public:
    string shiftingLetters(string S, vector<int>& shifts) {
        vector<int> total_shifts(S.length() + 1, 0);
        int n = S.length();
        for (int i = 0; i < n; ++i) {
          total_shifts[0] += (shifts[i] %= 26);
          total_shifts[i+1] -= (shifts[i] %= 26);
        }        
        total_shifts[0] %= 26;
        for (int i = 1; i < n; ++i) {
          total_shifts[i] += total_shifts[i-1];
          total_shifts[i] = (total_shifts[i] + 26)%26;
        }
        for (int i = 0; i < n; ++i) {
          S[i] = (S[i] + total_shifts[i] - 'a' + 26)%26 + 'a';
        }
        return S;
    }
};
