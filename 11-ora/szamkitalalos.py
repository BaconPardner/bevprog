import random


def main():
    print("I thought of a number between 1 and 100.")
    n = random.randrange(1, 100)
    guess = 0
    i = 0

    while (n != guess):
        guess = int(input("your guess> "))
        i += 1

        if n < guess:
            print("my number is smaller")
        elif n > guess:
            print("my number is larger")
        else:
            print("Good job! That's it!")
            print(f"Number of guesses: {i}")


if __name__ == "__main__":
    main()
