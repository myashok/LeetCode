class Solution {
public:
    bool checkPossibility(vector<int>& a) {
        int modified = false;
        for (int i = 1, prev = a[0]; i < a.size(); i++) {
            if (a[i] < prev && modified++) return false;
            if (a[i] < prev && i - 2 >= 0 && a[i - 2] > a[i]) continue;
            prev = a[i];
        }
        return true;
    }
};