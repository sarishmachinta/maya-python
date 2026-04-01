a1, a2, a3, b1, b2, b3 = map(int, input().split())
alice = sum(sorted([a1, a2, a3],reverse=True)[:2])
bob = sum(sorted([b1, b2, b3],reverse=True)[:2])
if alice > bob:
    print("Alice")
elif bob > alice:
    print("Bob")
else:
    print("Tie")
