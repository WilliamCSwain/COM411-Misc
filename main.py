# Print asks the user for their age
print("Please enter your age.")

# The user's response is read (Integer value due to numerical value)
age = int(input())

# Check if the user is an adult (18+)
if age >= 18:
    print("You are an adult.")
    print("This is due to you being 18 years or older.")
elif age >= 13:
    print("You are a teenager.")
    print("This is due to your age being 13 or above")
else:
    print("The age you entered is below 18.")
    print("You are therefore, not an adult.")
print("This is the end of the program.")