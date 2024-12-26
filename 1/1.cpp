#include <bits/stdc++.h>

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

typedef std::vector<int>* vp;

void readFile(std::string, vp, vp);
int partA(std::vector<int>, std::vector<int>);
int partB(std::vector<int>, std::vector<int>);

int main() {
    std::vector<int> a;
    std::vector<int> b;
    readFile("input.txt", &a, &b);

    std::cout << "Part A: " << partA(a, b) << '\n';
    std::cout << "Part B: " << partB(a, b) << '\n';

    return 0;
}

int partA(std::vector<int> a, std::vector<int> b) {
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int sum = 0;
    for (int i = 0; i < a.size(); i++) {
        sum += abs(a.at(i) - b.at(i));
    }

    return sum;
}

int partB(std::vector<int> a, std::vector<int> b) {
    std::map<int, int> map;
    for (int bN : b) {
        if (map.find(bN) == map.end()) {
            map[bN] = 1;
        } else {
            map[bN]++;
        }
    }

    int sum = 0;
    for (int aN : a) {
        sum += aN * map[aN];
    }

    return sum;
}

void readFile(std::string fileName, vp a, vp b) {
    std::ifstream file(fileName);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to open file: " + fileName);
    }

    std::string line;
    while (std::getline(file, line)) {
        int aN = std::stoi(line.substr(0, line.find(' ')));
        int bN = std::stoi(line.substr(line.find(' ') + 1));

        a->push_back(aN);
        b->push_back(bN);
    }

    file.close();
}