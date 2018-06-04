class Solution {
public:
    bool backspaceCompare(string S, string T) {
        string s = "", t = "";
        for (auto & x: S) {
            if (x == '#') { 
                if(s.length() > 0)
                    s.pop_back();
            }
            else s.push_back(x);                
        }
        for (auto & x: T) {
            if (x == '#') {
                if(t.length() > 0)
                    t.pop_back();
            }
            else t.push_back(x);                
        }
        cout << s << " " << t << endl;
        return s == t;
    }
};
