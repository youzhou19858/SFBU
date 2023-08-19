#include <cmath>
#include <iostream>

bool isPrime(int n) {
  if (n <= 1) return false;
  for (int i = 2; i <= sqrt(n); ++i) {
    if (n % i == 0) return false;
  }
  return true;
}

int main() {
  int n;
  std::cout << "Enter the upper limit: ";
  std::cin >> n;

  std::cout << "Twin Prime Pairs (difference of 2) up to " << n
            << " are:" << std::endl;
  for (int i = 2; i <= n - 2; ++i) {
    if (isPrime(i) && isPrime(i + 2)) {
      std::cout << "(" << i << ", " << i + 2 << ")" << std::endl;
    }
  }

  return 0;
}
