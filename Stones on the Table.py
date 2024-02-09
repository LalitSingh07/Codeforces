#Link :https://codeforces.com/problemset/problem/266/A

n = int(input())
stones = input()
count = 0
for x in range(1, n):
    if stones[x] == stones[x-1]:
        count += 1
print(count)