cost,dollors,bannas = map(int,input().split())
total = 0
for i in range(1,bannas+1):
    total += i*cost

if total > dollors:
    print(total - dollors)
else:
    print(0)