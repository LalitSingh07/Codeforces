rooms =  int(input())
count = 0
for i in range(rooms):
    p, q = map(int, input().split())
    if q - p >= 2:
        count += 1
print(count)
# Link :    https://codeforces.com/problemset/problem/467/A
# Time complexity: O(n)
