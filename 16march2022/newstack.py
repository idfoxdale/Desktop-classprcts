# Function to find substring of an input string
from itertools import permutations


def allPermutations(str):
    if len(str) > 1:  # Get all permutations of an input string # print all permutations
        permList = permutations(str, len(str) - 1)
        for perm in list(permList):
            print(''.join(perm))
            else:
                permList = permutations(str, len(str)-1)
            for perm in list(permList):
                print(''.join(perm))


# Driver program
if __name__ == "__main__":
    str = input("Please Enter a string: ")
    allPermutations(str)

vowels = ['a', 'e', 'i', 'o', 'u']
