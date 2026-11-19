import random

def main():

    firstNumCount = 0
    secondNumCount = 0
    while True:
        randomNum = random.randint(1, 2)

        if randomNum == 1:
            merakiOrGabi = "m"
            firstNumCount += 1
        elif randomNum == 2:
            merakiOrGabi = "g"
            secondNumCount += 1
        else:
            print("Invalid number!")

        print(f"Result: {merakiOrGabi}. Meraki appearances: {firstNumCount}. Gabi appearances: {secondNumCount}. Total instances: {firstNumCount + secondNumCount}")
        repeat = input("Generate another? (Y/N): ").lower()

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
