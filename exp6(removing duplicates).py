#Write a python program to remove all consecutive duplicates from a given string.
str = input()
result = str[0]
for i in range (1,len(str)):
    if str[i] != result[-1]:
        result += str[i]
print(result)
