# Asking the user whether it is sunny
print("Is it currently sunny?")
is_sunny = input()

print ("Is there currently a breeze?")
is_breeze = input().lower() # The .lower() part reads what the user typed and puts into lowercase

if is_sunny == "yes" and is_breeze == "yes":
        print("Your clothes are dry") # [R] if_sunny = yes, if_breeze = yes
elif is_sunny == "yes" and is_breeze == "no":
        print("Your clothes are drying slowly") # [R] if_sunny = yes, if_breeze = no
else:
    print("Your clothes are not dry.") # [R] if_sunny = no, if_breeze = no