n = int(input())
temp = 0
count = 0
for _ in range(n):  # Change the loop counter variable name to avoid overwriting `n`
    magnet = int(input())  # Rename `n` to `magnet`
    if magnet != temp:  # Update the condition to use `magnet`
        count += 1
    temp = magnet  # Update the assignment to use `magnet`
print(count)