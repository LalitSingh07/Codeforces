# This winter is so cold in Nvodsk! A group of n friends decided to buy k bottles of a soft drink called "Take-It-Light" to warm up a bit. Each bottle has l milliliters of the drink. Also they bought c limes and cut each of them into d slices. After that they found p grams of salt.

# To make a toast, each friend needs nl milliliters of the drink, a slice of lime and np grams of salt. The friends want to make as many toasts as they can, provided they all drink the same amount. How many toasts can each friend make?

# Input
# The first and only line contains positive integers n, k, l, c, d, p, nl, np, not exceeding 1000 and no less than 1. The numbers are separated by exactly one space.

# Output
# Print a single integer — the number of toasts each friend can make.
lists = list(map(int, input().split()))
n = lists[0]
k = lists[1]
l = lists[2]
c = lists[3]
d = lists[4]
p = lists[5]
nl = lists[6]
np = lists[7]

print(min(k*l//nl, c*d, p//np)//n)
