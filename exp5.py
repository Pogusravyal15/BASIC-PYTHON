#write a python program to add a key to dictionary.
import operator
d={}
n=int(input("no. of elements:"))
for i in range(n):
    k=input("enter key for first dictionary:")
    v=input("enter its value:")
    d[k]=v
key=input()
value=input()
d.update({key:value})
print(d)
