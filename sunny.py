# Asking the user whether it is sunny
print("Is it sunny?")
is_sunny = input()

print ("Is there a breeze?")
is_breeze = input().lower() # The .lower() part reads what the user typed and puts into lowercase

if is_sunny == "yes":
    if is_breeze == "yes":
        print("Clothes are dry") # if_sunny = yes, if_breeze = yes
    else:
        print("Clothes are drying slowly") # if_sunny = yes, if_breeze = no
else:
    print("Clothes are not drying") # if_sunny = no, if_breeze = no