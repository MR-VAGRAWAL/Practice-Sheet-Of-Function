#  1. Write a function to calculate area and perimeter of a rectangle.
area = (lambda length , breadth : length*breadth)
perimeter = (lambda length , breadth : 2*(length+breadth))
print(area(3,7))
print(perimeter(3,7))