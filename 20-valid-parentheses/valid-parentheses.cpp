#include <stack>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st; // Stack for opening brackets
        unordered_map<char, char> hash = {{')', '('}, {']', '['}, {'}', '{'}};
        
        for (char c : s) {
            if (hash.count(c)) { // If c is a closing bracket
                if (!st.empty() && st.top() == hash[c]) {
                    st.pop(); // Pop the matching opening bracket
                } else {
                    return false; // Invalid if no match
                }
            } else {
                st.push(c); // Push opening brackets
            }
        }
        return st.empty(); // Valid if stack is empty
    }
};