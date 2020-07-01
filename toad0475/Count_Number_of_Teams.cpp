// submission : https://leetcode.com/submissions/detail/360468066/

/* 설명
O(n^2) 솔루션,
현재 index의 값이 이전 index의 값보다 작은값, 큰값이 각각 몇개씩 있는지 구하고,
현재 index의 값이 이후 index의 값보다 작은값, 큰값이 각각 몇개씩 있는지 구해서,
각각의 개수를 누적하는데,

경우의 수를 전부 조사해야 하므로

(이전 Index중 작은값 개수) * (이후 Index중 큰값의 개수) + (이후 Index중 작은값 개수) * (이전 index중 큰값의 개수)
위와 같은 공식으로 계산해서 누적한 다음
최종으로 누적된 값을 반환함
*/

class Solution {
public:
    int numTeams(vector<int>& rating) {
        int answer = 0;
            
        for (int i=1; i<rating.size(); i++)
        {
            int less[2] = {}, greater[2] = {};
            for (int j=0; j<rating.size(); j++)
            {
                less[i<j] += rating[i] < rating[j];
                greater[i<j] += rating[i] > rating[j];
                
            }
            answer += less[0] * greater[1] + less[1] * greater[0];
        }
        return answer;
    }
};
