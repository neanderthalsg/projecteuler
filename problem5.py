# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# input - Not applicable

# process

counter = 0
number = 2521
done = False

while done == False:
     for i in range(1,21):
         if number%i ==0:
             counter = counter + 1

     if counter == 20:
         done = True
     else:
       number = number + 1
       counter = 0

# output
print("The number is:", number)
