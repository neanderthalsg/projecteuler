# Euler 25 - What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# Input - Not applicable

# Process

firstTerm = 1
secondTerm = 1
sum = 0
counter = 2

while len(str(sum)) < 1000:
    sum = firstTerm + secondTerm
    firstTerm = secondTerm
    secondTerm = sum
    counter += 1


# Output
# print("The number is:", sum)
print("The first Index of 1000 digits:", counter)
