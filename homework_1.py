def is_triangle(a, b, c):
    if a + b < c or b + c < a or c + a < b:
        return False
    else:
        return True
a = 3
b = 4
c = 5
if is_triangle(a, b, c) == True:
    print("Треугольник существует")    
else:
    print("Треугольник не существует")

if is_triangle(a, b, c) == True:
    if a==b==c:
        print("Треугольник является равносторонним")
    elif a==b or a==c or b==c:
        print("Треугольник является равнобедренным")
    else:
        print("Треугольник является разносторонним")