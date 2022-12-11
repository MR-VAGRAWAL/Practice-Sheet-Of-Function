#  5. Write a function to check if a number is even or not.
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input())
print(even_odd(num))