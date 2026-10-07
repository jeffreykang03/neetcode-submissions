class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if (m == 0) return false;
        int n = matrix[0].size();
        if (n == 0) return false;

        // 1) Binary search to find the candidate row
        int l = 0, r = m - 1;
        int row = -1;
        while (l <= r) {
            int c = l + (r - l) / 2;
            if (target > matrix[c][n - 1]) {
                l = c + 1;            // target is to the "down" side
            } else if (target < matrix[c][0]) {
                r = c - 1;            // target is to the "up" side
            } else {
                row = c;              // target fits in this row's range
                break;                // IMPORTANT: stop searching rows
            }
        }
        if (row == -1) return false;

        // 2) Binary search within the row
        l = 0; r = n - 1;
        while (l <= r) {
            int c = l + (r - l) / 2;
            if (matrix[row][c] < target) {
                l = c + 1;
            } else if (matrix[row][c] > target) {
                r = c - 1;
            } else {
                return true;
            }
        }
        return false;
    }
};