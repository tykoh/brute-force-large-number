"""
1. Accept a numeric input within the selection 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096
2. Generate a random number within the range of the input bits
3. Execute method to brute force the random number and output time taken
4. Create unit test to test the brute force method
"""

import random
import time


def brute_force(number, largest_number):
    """
    Brute force the random number
    """
    running_symbol = "|/-\\"
    print("Brute forcing the random number")
    start = time.time()
    for i in range(0, number + 1):
        # print percentage of test run
        print(
            running_symbol[i % len(running_symbol)],
            "Percentage: " + str(round((i / largest_number) * 100, 5)) + "%",
            end="\r",
        )

        if i == number:
            # print new line
            print("Brute force complete          ")
            print("The number is: " + str(i))
            end = time.time()
            # print time in milliseconds
            print("Time taken: " + str(round((end - start) * 1000, 5)) + "ms")

            break


def generate_random_number_with_bits(number_of_bits):
    """
    Generate a random number with the number of bits
    """
    largest_number = 2**number_of_bits
    print("Generating a random number with " + str(number_of_bits) + " bits")
    print("The largest number is: " + str(largest_number))
    random_number = random.randint(0, largest_number)
    return random_number, largest_number


def main():
    """
    Main method
    """
    number_of_bits = int(
        input(
            "Enter number of bits for random number \nSupported: 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096): "
        )
    )
    if not number_of_bits in [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:
        print(
            "Invalid input. \nSupported: 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096"
        )
        return
    random_number, largest_number = generate_random_number_with_bits(number_of_bits)
    brute_force(random_number, largest_number)


if __name__ == "__main__":
    main()
