import random

# def guess(x):
#     random_number=random.randint(1,x)
#     guess=0

#     while guess != random_number:
#         guess=int(input(f"Guess a random number between 1 and {x}:"))
#         if guess<random_number:
#             print("Too low.Guess again ☹️")
#         elif guess > random_number:
#             print("Too high.Guess again 🚀")
    
#     print(
#         f"Congratulations! You guessed the correct number {random_number} "
#     )

# guess(10)


def computer_guess (x):
    low=1
    high=x
    feedback=""

    while feedback!="c":
        guess=random.randint(low,high)
        feedback=input(f"Is {guess } to High (H) or low(L) or correct(C)??").lower()

        if feedback=="h":
            high=guess-1
        elif feedback=="l":
            low=guess+1
    
    print("Yay you guessed it correctly🔥🔥")

computer_guess(20)