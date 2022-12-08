#  3. Write a function to calculate power of a number raised to other. 
base_power = lambda base , power : base ** power
base = int(input())
power = int(input())
print(base_power(base , power))