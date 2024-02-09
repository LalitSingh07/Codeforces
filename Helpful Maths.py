lst = list(map(int, input().split("+")))    
lst.sort()

print("+" .join(str(x) for x in lst))