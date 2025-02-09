x = input()
a, b = map(int, input().split())
maximum = max(a, b)
y = 6 - maximum + 1
from math import gcd
g = gcd(y, 6)
print(f"{y // g}/{6 // g}")