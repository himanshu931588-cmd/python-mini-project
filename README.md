# ⚡ Python vs C++ Prime Number Benchmark

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![C++17](https://img.shields.io/badge/C%2B%2B-17-blue.svg)](https://isocpp.org/)

## 📌 Overview

A **performance benchmarking tool** that computes the first 10,000 prime numbers in both **Python** and **C++**, then displays a beautiful comparison dashboard. Perfect for understanding why compiled languages excel at CPU-bound tasks.

### 🎯 What You'll Learn
- Why C++ is 5-20x faster for mathematical computations
- How to call C++ code from Python using subprocess
- Basic benchmarking and performance analysis
- Language trade-offs: development speed vs execution speed

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.7+** (any distribution)
- **g++ compiler** (for C++)
  - Linux/macOS: Usually pre-installed
  - Windows: Install [MinGW-w64](https://www.mingw-w64.org/) or use WSL

### Installation

```bash
# Clone the repository
git clone https://github.com/himanshu931588-cmd/python-mini-project.git
cd benchmark-primes

# No additional libraries needed! (pure Python standard library)