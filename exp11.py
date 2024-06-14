#Write a python program to combine two dictionary adding values for common keys.
dict1={'a':10,'b':20,'c':30}
dict2={'b':10,'c':20,'d':30}
combined_dict={}
for key in dict1:
    if key in dict2:
        combined_dict[key]=dict1[key]+dict2[key]
    else:
        combined_dict[key]=dict1[key]
        
for key in dict2:
    if key not in combined_dict:
        combined_dict[key]=dict2[key]
        
print("combined dictionary:",combined_dict)
