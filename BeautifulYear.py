
#Link https://codeforces.com/problemset/problem/271/A


n = int(input())
while True:
    n += 1
    if len(set(str(n))) == 4:
        break
print(n)

