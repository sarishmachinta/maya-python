N,M =map(int,input().split())
online_price = 0.9 * N 
if online_price < M:
    print("ONLINE")
elif online_price > M:
    print("DINING")
else:
    print("EITHER")
