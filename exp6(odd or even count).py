#Print the elements in the list which has occured odd number of times.
a=input().split()
b=[]
for i in a:
    if a.count(i)%2 !=0 and i not in b:
        b.append(i)
print(b)


elements = [4,7,5,2,2,5,5,7,3,7,4]
counts = {}
for element in elements:
    if element in counts:
        counts[element] += 1
    else:
        counts[element] = 1
for element, count in counts.items():
    if count % 2 != 0:
        print(element)
