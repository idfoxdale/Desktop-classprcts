# Function to find substring of an input string
from itertools import permutations

def allPermutations(str):
	
	# Get all permutations of an input string
	permList = permutations(str)

	# print all permutations
	for perm in list(permList):
		print (''.join(perm))
		
# Driver program
if __name__ == "__main__":
	str = input("Please Enter a string: ")
	allPermutations(str)

