#  6. Write a function to check if a number is prime or not.
def prime(num):
    count = 0
    for i in range(1,num+1):
        if num == 1:
            return "UNDEFINED"
        elif num % i == 0:
            count += 1
    if count == 2:
        return "PRIME"
    else:
        return "NOT PRIME"
num = int(input())
print(prime(num))