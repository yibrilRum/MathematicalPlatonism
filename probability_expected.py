import random

def main():
    
    firstNumCount = 0
    secondNumCount = 0
    while True:
        randomNum = random.randint(1, 2)

        if randomNum == 1:
            firstNumCount += 1
        elif randomNum == 2:
        secondNumCount += 1
        else:
            print("Invalid number!")

        print(f"Random number: {randomNum}. 1 appearances: {firstNumCount}. 2 appearances: {secondNumCount}. Total instances: {firstNumCount + secondNumCount}")
        repeat = input("Generate another random number? (Y/N): ").lower()

        if repeat == "y":
            pass
        if repeat == "":
            pass
        elif repeat == "n":
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
