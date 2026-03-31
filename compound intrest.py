p = int(input())
r = int(input())
t = int(input())
amount = p * (1 + r/100) ** t
ci = amount - p
print(f"{ci:.2f}")
