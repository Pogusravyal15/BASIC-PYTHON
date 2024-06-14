#Write a python program to merge two python dictionaries.
d1={1:2,3:4}
d2={5:6}
d3=d1.copy()
d3.update(d2)
print(d3)

d={}
d1={}
n=int(input("no of elements"))
for i in range(n):
    k=input("enter key for dict:")
    v=input("enter its value:")
    d[k]=v
for i in range(n):
    k=input("enter key for dict:")
    v=input("enter its value:")
    d1[k]=v
d2=d.copy()
d2.update(d1)
print(d2)
