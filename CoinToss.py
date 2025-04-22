import random

# Constants
HEADS = 1
TAILS = 2
TOSSES = 10  # Total number of tosses to simulate

def main():
    print("Coin Toss Simulator\n")

    for toss_num in range(1, TOSSES + 1):
        result = random.randint(HEADS, TAILS)
        if result == HEADS:
            print(f"Toss {toss_num}: Heads")
        else:
            print(f"Toss {toss_num}: Tails")

    print("\nSimulation complete.")

if __name__ == "__main__":
    main()
