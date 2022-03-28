from MyModule import circle, square, triangle
if __name__ == '__main__':
    triangle = triangle(5, 6, 8)
    print('surface =', triangle.surface(), 'circuit =', triangle.circuit())
    circle = circle(3)
    print('surface =', circle.surface(), 'circuit =', circle.circuit())
    square = square(7)
    print('surface =', square.surface(), 'circuit =', square.circuit())