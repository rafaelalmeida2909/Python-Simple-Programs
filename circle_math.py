import math

print("===== Circle Calculator =====")

r = float(input("\nInput Radius: "))

print(f"\nRadius = {r:.2f}")
print(f"Length = {2 * math.pi * r:.2f}")
print(f"Area = {math.pi * r * r:.2f}")