a = int(input())
b = int(input())
ans = 0

for i in range(a if a % 2 == 0 else a + 1, b + 1 if b % 2 == 0 else b, 2):
    ans += i

print(ans)
