#https://codeforces.com/problemset/problem/263/A
# Link: https://codeforces.com/problemset/problem/263/A
matrix = []
for x in range(5):
    matrix.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            print(abs(2-i)+abs(2-j))
            break