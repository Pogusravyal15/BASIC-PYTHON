d={1:'hi', 'a':123, 100:32.4}
#accessing dictionary using key
print(d[1])
print(d['a'])
print(d[100])
#accessing element using get()
print(d.get('a'))
#accessing dictionary using loops
for i in d:
    print(i,":",d[i])
