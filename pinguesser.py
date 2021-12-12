import random

def guess(pin,attempts):
    correct = []
    userguess = input(f"Input your {attempts} guess with a space between characters.").split(" ")
    correct = ["Correct" if str(num) == userguess[i] else "Incorrect" for i,num in enumerate(pin)]
    print(correct)
    print(f"Good job! The pin was {pin} and this took you {attempts} tries!") if "Incorrect" not in correct else guess(pin,attempts+1)

def main():
    pin = [random.randint(0,9) for _ in range(4)]
    guess(pin,1)

if __name__ == "__main__": main()