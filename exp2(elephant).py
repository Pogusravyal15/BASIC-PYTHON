x = int(input("Enter the coordinate of the friend's house: "));
steps = x // 5 # It is used to calculates the number of full steps of size 5 by using integer division.
if x % 5 != 0: # checks if the remainder when x is divided by 5 is not zero.
    steps += 1
print("The steps are: ",steps)
