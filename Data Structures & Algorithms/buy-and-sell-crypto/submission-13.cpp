class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int p1 = 0; int p2 = 1;
        int profit = 0;
        while(p1 < prices.size()-1){ 
            while(prices[p1] > prices[p2]){
                p1++;
                p2++;
                //cout << p1 << " " << p2 << " a" << endl;
            }
            while(prices[p1] < prices[p2] && p2 < prices.size()){
                profit = max(profit, prices[p2] - prices[p1]);
                p2++;
                //cout << p1 << " " << p2 << " b" << endl;
            }
            //cout << p1 << " " << p2 << " c" << endl;
            if(p1 == p2)
                break;
            p1 = p2;
            p2++;
        }
        return profit;
    }
};
