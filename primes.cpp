#include <iostream>
#include <chrono>
#include <vector>
#include <cmath>

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

int main() {
    int count = 0;
    int num = 2;
    const int TARGET = 10000;
    
    auto start = std::chrono::high_resolution_clock::now();
    
    while (count < TARGET) {
        if (isPrime(num)) count++;
        num++;
    }
    
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    
    std::cout << elapsed.count() << std::endl;
    return 0;
}