import argparse
import time
from math import isqrt

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, isqrt(n) + 1, 2):
        if n % i == 0: return False
    return True

def sushiki_next_prime(target):
    candidate = target if target % 2 == 1 else target + 1
    start = time.time()
    while not is_prime(candidate):
        candidate += 2
    elapsed = time.time() - start
    return candidate, elapsed

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=int, required=True)
    args = parser.parse_args()
    
    result, t = sushiki_next_prime(args.target)
    true_next = 100000000000000039
    
    print(f"Target: {args.target}")
    print(f"Sushiki: {result}")
    print(f"True   : {true_next}")
    print(f"Match  : {result == true_next}")
    print(f"Error  : {abs(result - true_next)}")
    print(f"Time   : {t:.2f}s")
