# Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
# number and if the cube of that number is divisible by 4 or 
#
numbers = list(range(1,101)) #list of numbers from 1 to 100
cubes_divisible_by_4_or_5 = [] #enplty list to store numbers whose cubes are divisible by 4 or 5

for num in numbers :
    cube = num ** 3
    if cube % 4 == 0 or cube % 5 == 0 :
        cubes_divisible_by_4_or_5.append(num)

print("numbers whose cubes are divisible by 4 or 5 (using for loop):" , cubes_divisible_by_4_or_5)

#using while loop 
numbers = list(range(1, 101))  # List of numbers from 1 to 100
cubes_divisible_by_4_or_5 = []  # Empty list to store numbers whose cubes are divisible by 4 or 5

index = 0
while index < len(numbers):
    num = numbers[index]
    cube = num ** 3
    if cube % 4 == 0 or cube % 5 == 0:
        cubes_divisible_by_4_or_5.append(num)
    index += 1

print("Numbers whose cubes are divisible by 4 or 5 (using while loop):")
print(cubes_divisible_by_4_or_5)
