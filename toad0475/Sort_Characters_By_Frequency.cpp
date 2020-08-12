// submission: https://leetcode.com/submissions/detail/379615726/

// map에 각 char를 카운팅하여 담고, 
// char별로 map에 카운팅한 개수 번 만큼 새로운 버켓에 일렬로 기록한 다음,
// answer 스트링에 기록하는 알고리즘인데..

// bucket[n].append(n,c); 이 부분을 이해 못했음 자동으로 Sort가 어떻게 이루어 지는건지..

class Solution {
public:
    string frequencySort(string s) {
        map<char, int> freqmap;
        vector<string> bucket(s.size()+1, "");
        string answer;
        
        for (char c:s){
            freqmap[c]++;      
        }
        
        for(auto& it:freqmap){
            char c = it.first;
            int n = it.second;
            bucket[n].append(n,c);
        }
        
        for(int i=s.size(); i>0; i--){
            answer.append(bucket[i]);
        }
        
        return answer;
    }
};
