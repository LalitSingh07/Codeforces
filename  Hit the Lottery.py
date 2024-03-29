# A. Hit the Lottery
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Allen has a LOT of money. He has n
#  dollars in the bank. For security reasons, he wants to withdraw it in cash (we will not disclose the reasons here). The denominations for dollar bills are 1
# , 5
# , 10
# , 20
# , 100
# . What is the minimum number of bills Allen could receive after withdrawing his entire balance?

# Input
# The first and only line of input contains a single integer n
#  (1≤n≤109
# ).

# Output
# Output the minimum number of bills that Allen could receive.

n = int(input())
count = 0
denominations = [100, 20, 10, 5, 1]

for denomination in denominations:
    count += n // denomination
    n %= denomination

print(count)