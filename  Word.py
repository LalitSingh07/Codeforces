
word = input()

lower = sum(1 for c in word if c.islower())
upper = sum(1 for c in word if c.isupper())

if lower == upper or lower > upper:
    print(word.lower())
else:
    print(word.upper())



