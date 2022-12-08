#  2. Write a function to calculate area and circumference of a circle.
area = lambda radius : 3.14*radius**2
perimeter = lambda radius : 2*3.14*radius
radius = eval(input())
print(area(radius))
print(perimeter(radius))