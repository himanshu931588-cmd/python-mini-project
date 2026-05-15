import subprocess
import time
import sys
import os
import platform

def find_primes_python(n=10000):
    """Pure Python implementation for benchmarking"""
    def is_prime(num):
        if num <= 1: return False
        if num <= 3: return True
        if num % 2 == 0 or num % 3 == 0: return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    count = 0
    num = 2
    start = time.perf_counter()
    while count < n:
        if is_prime(num):
            count += 1
        num += 1
    end = time.perf_counter()
    return end - start

def compile_cpp_windows():
    """Compile C++ code on Windows using MSVC or g++"""
    cpp_file = os.path.join("cpp_core", "primes.cpp")
    exe_file = os.path.join("cpp_core", "prime_runner.exe")
    
    # Try different compilers
    compilers = [
        ["g++", "-O2", "-std=c++17", cpp_file, "-o", exe_file],  # MinGW
        ["cl", "/O2", "/std:c++17", cpp_file, "/Fe:" + exe_file],  # MSVC
        ["clang++", "-O2", "-std=c++17", cpp_file, "-o", exe_file]  # Clang
    ]
    
    for compiler_cmd in compilers:
        try:
            print(f"🛠️ Trying to compile with: {compiler_cmd[0]}...")
            result = subprocess.run(compiler_cmd, cwd=".", capture_output=True, text=True, shell=True)
            if result.returncode == 0 and os.path.exists(exe_file):
                print(f"✅ Compilation successful with {compiler_cmd[0]}!")
                return True
        except FileNotFoundError:
            continue
    
    print("❌ No C++ compiler found. Please install MinGW or Visual Studio Build Tools.")
    print("\n📥 Installation options:")
    print("1. MinGW: https://www.mingw-w64.org/")
    print("2. Visual Studio Build Tools: https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022")
    return False

def compile_cpp_unix():
    """Compile C++ code on Linux/macOS"""
    result = subprocess.run(["make", "-C", "cpp_core"], capture_output=True, text=True)
    return result.returncode == 0

def run_cpp_benchmark():
    """Compile and run C++ prime counter"""
    cpp_dir = "cpp_core"
    exe_name = "prime_runner.exe" if platform.system() == "Windows" else "prime_runner"
    binary = os.path.join(cpp_dir, exe_name)
    cpp_file = os.path.join(cpp_dir, "primes.cpp")
    
    # Check if compilation is needed
    need_compile = False
    if not os.path.exists(binary):
        need_compile = True
    elif os.path.exists(cpp_file):
        if os.path.getmtime(cpp_file) > os.path.getmtime(binary):
            need_compile = True
    
    if need_compile:
        print("🛠️ Compiling C++ code...")
        if platform.system() == "Windows":
            success = compile_cpp_windows()
        else:
            success = compile_cpp_unix()
        
        if not success:
            return None
    
    # Run benchmark
    try:
        result = subprocess.run(["./" + binary if platform.system() != "Windows" else binary], 
                              cwd=cpp_dir, 
                              capture_output=True, 
                              text=True,
                              shell=True)
        if result.returncode == 0:
            return float(result.stdout.strip())
        else:
            print("❌ C++ runtime error:", result.stderr)
            return None
    except Exception as e:
        print(f"❌ Error running C++ binary: {e}")
        return None

def display_dashboard(py_time, cpp_time):
    """Simple CLI dashboard"""
    print("\n" + "="*50)
    print("⚡ BENCHMARK DASHBOARD ⚡".center(50))
    print("="*50)
    print(f"🐍 Python Time   : {py_time:.4f} seconds")
    if cpp_time:
        print(f"⚙️  C++ Time      : {cpp_time:.4f} seconds")
        speedup = py_time / cpp_time
        print(f"🚀 Speedup (C++ vs Python): {speedup:.2f}x")
        print("\n💡 Insight: C++ is much faster for CPU-bound tasks like prime computation.")
    else:
        print("⚙️  C++ Time      : Failed to compile/run")
        print("\n💡 Tip: Install MinGW or use WSL for C++ benchmarking")
    print("="*50)

if __name__ == "__main__":
    print("🔍 Benchmarking first 10,000 prime numbers...\n")
    
    py_time = find_primes_python()
    print(f"✅ Python completed in {py_time:.4f}s")
    
    cpp_time = run_cpp_benchmark()
    if cpp_time:
        print(f"✅ C++ completed in {cpp_time:.4f}s")
    
    display_dashboard(py_time, cpp_time)