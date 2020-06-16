// submission : https://leetcode.com/submissions/detail/354456827/
// ".push_back" adds a new element at the end of the vector, after its current last element.

class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> arr;
        for(int i=0;i<n;i++)
        {
            arr.push_back(nums[i]);
            arr.push_back(nums[i+n]);
            
        }
       return arr;
    }
};

