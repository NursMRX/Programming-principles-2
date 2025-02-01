import random 
    
random_num = random.randint(1, 20)
print("Hello! What is your name?")
name = str(input())
print(f"Well {name}, I am thinking of a number betweem 1 to 20")
count = 1
while True:
    guess_number = input("Take a guess: ")
        
    if guess_number.lower() == 'q':
        print("Goodbye!")
        break
    if not guess_number.isdigit():
        print("Please enter a number!")
        continue
        
    guess_num = int(guess_number)
        
    if guess_num < random_num:
        print("Your guess is too low")
        count += 1
    elif guess_num > random_num:
        print("Your guess id too high")
        count += 1
    else:
        print(f"Good job, {name}! You guessed my number in {count} guesses!")
        break