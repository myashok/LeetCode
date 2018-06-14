class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int curr(0), mx(0);
        int p=0, s=seats.size()-1;
        for (; p < seats.size(); ++p) {
            if(seats[p] == 1) break;
        }
        mx = p;
        for (; s >= 0; --s) {
            if(seats[s] == 1) break;
        }
        mx = max(mx, (int)(seats.size()-1) - s);
        for (; p <= s; ++p) {
            curr = (seats[p] == 0) ? curr + 1: 0;
            mx = max((curr+1)/2, mx);
        }
        return mx;
    }
};
