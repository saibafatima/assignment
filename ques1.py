# Q1. Explain with an example each when to use a for loop and a while loop.

# for loop  is used for iteration  
numbers = [1, 2, 3, 4, 5]
sum_result = 0

for num in numbers:
    sum_result += num

print("Sum of the numbers:", sum_result)

#  while loop is ---> iterate based on some conditions
num = 5
factorial = 1
count = 1

while count <= num:
    factorial *= count
    count += 1

print("Factorial of", num, "is", factorial)
