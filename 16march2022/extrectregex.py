# importing the regex module
import re

# opening and reading the file
with open('Feb 07 5_28 PM.txt') as fh:
    fstring = fh.readlines()

# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# initializing the list object
lst=[]

# extracting the IP addresses
for line in fstring:
    lst.append(pattern.search(line)[0])

# displaying the extracted IP addresses
print(lst)