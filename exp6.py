#write a python program to check whether a given key already exists in a dictionary.
import operator
d={}
n=int(input("no. of elements:"))
for i in range(n):
    k=input("enter key for first dictionary:")
    v=input("enter its value:")
    d[k]=v
key=input()
if key in d:
    print('Key is present in the dictionary')
else:
    print('Key is not present in the dictionary')
