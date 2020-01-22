l1 = [3, 1, 4, 2, 5]

for i in range(len(l1)):
    for j in range(i + 1, len(l1)):

        if l1[i] > l1[j]:
           l1[i], l1[j] = l1[j], l1[i]

print (l1)