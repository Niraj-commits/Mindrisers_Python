
# Todo: Create a function that takes multiple numbers and print the sum of the numbers using *num

def numbers(*num):
    summation = 0
    for number in num:
        summation += number
    return summation

result = numbers(5,6,7,8,9)

print(result)