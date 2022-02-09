#include <iostream>
#include <string>
int getPlatoonCount(int startNumber) {
    if(startNumber<3) {
        return startNumber;
    }
    return startNumber + getPlatoonCount(startNumber - 2);
}
int main() {
    for (std::string line; std::getline(std::cin, line);) {
        int firstRowCount = atoi(line.c_str());
        std::cout << getPlatoonCount(firstRowCount)<< std::endl; // print the answer as stdout
    }
    return 0;
}