N = int(input("Enter the value of N: "))
total_sum = 0
for i in range(1, N + 1):
    total_sum += i
    print(f"The sum of the first {N} natural numbers is: {total_sum}")
