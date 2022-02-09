#include <iostream>
#include <string>
#include <sstream>

using namespace std;

void subs(string& str, int num) {
    ostringstream ss;
    ss << num;
    str+=ss.str();
    str.push_back(',');
}

string encodeString(string inp) {
    int upperCaseStart_ = (int)'A'-1;
    int lowerCaseStart_ = (int)'a'-1;
    string out = "";
    for (int i=0;i<inp.length();i++) {
        if(inp[i] >= 'a' && inp[i] <='z') {
            subs(out, inp[i] - lowerCaseStart_);
        }
        if(inp[i] >= 'A' && inp[i] <='Z') {
            subs(out, inp[i] - upperCaseStart_);
        }
        if(inp[i] >= '0' && inp[i] <='9') {
            out.push_back(inp[i]);
        }
    }
    if (out.length()) {
        //out.pop_back();
        out = out.substr(0, out.size()-1);
    }
    return out;
}

int main() {
    for (std::string line; std::getline(std::cin, line);) { // get the line
        //here your code
        std::cout << encodeString(line) << std::endl; // print the answer as stdout
    }
    return 0;
}