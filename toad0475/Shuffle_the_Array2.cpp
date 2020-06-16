// submission : https://leetcode.com/problems/shuffle-the-array/submissions/

class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> answer(n*2);
        
        for (int i=0, j=0; i<n; i++)
        {
            answer[j++]=nums[i];
            answer[j++]=nums[n+i];
        }
        return answer;
    }
};
