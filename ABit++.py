# Link: https://codeforces.com/problemset/problem/282/A
operations =[]
n = int(input())
for x in range(n):
    operations.append(input())

count = 0
for i in range(n):
    if operations[i] == "++X" or operations[i] == "X++":
        count+=1
    else:
        count-=1
print(count)
