class Solution {
public:
    int search(vector<int>& arr, int target) {
       int low = 0;
       int high = arr.size()-1;
       while (low <= high) {
          int mid = (low + high)   / 2;
          if (arr[mid] == target) return mid;
          
           if (arr[mid] >= arr[low]) {
              if (arr[mid] > target and arr[low] <= target) {
                  high = mid-1;
              } else {
                  low = mid+1;
              }
          } else {
              if (arr[high] >= target and arr[mid] < target) {
                  low = mid+1;
              } else {
                  high = mid-1;
              }
          }
        }
        return -1;
    }
};
