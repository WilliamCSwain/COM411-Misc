# Asking the user whether it is sunny.
print("Is it sunny?")
is_sunny = input()

print ("Is there a breeze?")
is_breeze = input().lower() # The .lower() part reads what the user typed and puts into lowercase

if is_sunny == "yes":
    if is_breeze == "yes":
        print("Clothes are dry")
    else:
        print("Clothes are drying slowly")
else:
    print("Clothes are not drying")