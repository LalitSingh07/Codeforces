n = int(input())
list =[]
for x in range(n):
    list.append(input())

for word in list:
    if(len(word)>10):
        length = str(len(word)-2)
        print(word[0]+length+word[-1])
    else:
        print(word)

   
