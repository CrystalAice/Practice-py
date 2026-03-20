guess_count = 0
Easy = 10
Medium = 5
Hard = 3
answer = 28
print("Please select the difficulty level: \n1. Easy 10 chances \n2. Medium 5 chances \n3. Hard 3 chances\n")
choice = int(input("Enter your choice: "))
if choice == 1:
    guess_max = Easy
if choice == 2:
    guess_max = Medium
if choice == 3:
    guess_max = Hard

while guess_count < guess_max :
    num = int(input("\nEnter a number: "))
    guess_count += 1
    if num > answer:
        print("too high")
    elif  num < answer:
        print("too low")
    else:
        print("you guessed right")
        break
else:
    print("You ran out of guesses")










