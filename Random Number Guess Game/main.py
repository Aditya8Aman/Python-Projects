'''Its a game where you guess a random number between 1 to 99 using instructions from computer about the previous
# guess being higher or lower than the random number'''
import random
ranNumber = random.randint(1,100)
guess=0
while (True):
    num = int(input("Enter you number:"))
    if num == ranNumber:
        print(f"You guessed the correct random number:{num} in {guess} guess")
        break
    elif num>ranNumber:
        print("Its lower than that")

    else:
        print("Its higher than that")

    guess+=1
with open("hiscore.txt",'r') as f:
    hs=int(f.read())

if guess<hs:
    with open("hiscore.txt","w") as f:
        f.write(str(guess))
