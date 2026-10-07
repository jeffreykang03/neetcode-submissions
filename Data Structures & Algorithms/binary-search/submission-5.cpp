class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size()-1;
        while(l<=r){
            int cur = l + ((r-l)/2);
            if(target < nums[cur]){
                r = cur-1;
            } 
            else if(target > nums[cur]){
                l = cur+1;
            }
            else {
                return cur; 
            }
            //cout << l << " " << r << endl;
        }
        return -1;
    }
};
