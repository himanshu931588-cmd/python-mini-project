CXX = g++
CXXFLAGS = -O2 -std=c++17
TARGET = prime_runner

$(TARGET): primes.cpp
	$(CXX) $(CXXFLAGS) -o $(TARGET) primes.cpp

clean:
	rm -f $(TARGET)