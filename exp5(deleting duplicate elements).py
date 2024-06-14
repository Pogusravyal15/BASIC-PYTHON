#Print the list after deleting the duplicate elements in it.
l = [1, 2, 3, 2, 3, 55, 13, 14, 1, 8, 1, 4]
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
