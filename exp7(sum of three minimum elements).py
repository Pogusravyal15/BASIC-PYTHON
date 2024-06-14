#Read a list and print sum of three minimum elements in the list.
a=list(map(int,input().split()))
a.sort()
print(sum(a[:3]))


