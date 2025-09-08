import random

code3=[random.randint(0,9) for _ in range(3)]
code4=[random.randint(1,6) for _ in range(4)]
print(f"3-digit code(0-9):{code3}")
print(f"4-digit code(1-6):{code4}")