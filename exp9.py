#Write a python program to remove a key from a dictionary.
d={}
n=int(input("no of elements"))
for i in range(n):
    k=int(input("enter key for dict:"))
    v=int(input("enter its value:"))
    d[k]=v
key=int(input())
if key in d:
    del d[key]
print(d)
