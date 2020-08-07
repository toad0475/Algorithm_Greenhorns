
// in progress...



class Solution {
public:
    string frequencySort(string s) {
        map<char, int> charmap;
        
        for (int i = 0 ; i != s.size(); i++){
            charmap[s[i]] = charmap[s[i]]+1;
            
        }
        
        for(auto it = charmap.cbegin(); it != charmap.cend(); ++it){
            cout << it;
        }
        
        
        
        
    return s;
    }
};
