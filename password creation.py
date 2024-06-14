correct_password = "hello_sravya"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    inputp = input("Enter your password: ")
    if inputp == correct_password:
        print("Correct password")
        break
    else:
        attempts += 1
        print("Incorrect password. You have", max_attempts - attempts, "attempt(s) left.")

# If the user fails to enter the correct password within the maximum attempts
if attempts == max_attempts:
    print("Locked")

