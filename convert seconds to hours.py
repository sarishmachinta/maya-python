s = int(input())
h = s // 3600
r = s% 3600
m = r // 60
sec = r % 60
print("H:M:S-{}:{}:{}".format(h ,m, sec))
