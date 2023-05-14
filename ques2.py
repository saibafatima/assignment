# Q2. Write a python program to print the sum and product of the first 10 natural numbers using for
# and while loop.

# by using for loop
numbers = range(1,11) #numbers from 1 to 10 
sum_result = 0
product_result = 1

for num in numbers :
    sum_result += num
    product_result *= num

print("sum of 1st 10 natural numbers:", sum_result)
print("product of 1st 10 natural numbers", product_result)

#by using while loop 
count = 1
sum = 0
product = 1
while count <= 10 :
    sum += count
    product *= count
    count += 1

print("sum of 1st 10 natural number using while loop  is :", sum)
print("product of 1st 10 natural number using while loop is:", product)


