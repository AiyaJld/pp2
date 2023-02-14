import random
def number(num):
    counter=1
    rand=random.randint(1,20)
    while True:
        if num==rand:
            print("Good job,"," ",name,"! ","You guessed my number in"," ",counter," guesses!",sep="")
            break
        elif num<rand:
            print("Your guess is too low.")
            print("Take a guess")
            num=int(input())
            counter+=1
        elif number>rand:
            print("Your guess is too high.")
            print("Take a guess")
            num=int(input())
            counter+=1
print("Hello! What is your name?")
name=input()
print("Well", name, "I am thinking of a number between 1 and 20.", sep=", ")
print("Take a guess.")
number=int(input())
number(number)