import random

rvalues = random.randint(1,9)
print(rvalues)

guess = int(input("Enter a guessfrom 1 to 9: "))

if guess == rvalues:
       print("Right value")
elif guess < rvalues :
        print("Very low value")
else:
        print("High value")
        
