#Write a python program to map two lists into a dictionary.
d = [1,2,3,4,5,6,7,8,9]
d1 = [9,8,7,6,5,4,3,2,1]
s = {d[i]: d1[i] for i in range(len(d))}
print("Mapped Dictionary:", s)


keys=input().split()
values=input().split()
d=dict(zip(keys,values))
print(d)
