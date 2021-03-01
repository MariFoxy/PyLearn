import math

# функция для расчета расстояния между центром и заданной точкой
def check(cx, cy, cz, x, y, z):
    x1 = math.pow((x-cx), 2)
    y1 = math.pow((y-cy), 2)
    z1 = math.pow((z-cz), 2)
    return (x1 + y1 + z1) # расстояние между центром и заданной точкой

cx = -0.5

cy = 1 # координаты центра

cz = -1.99

r = 91.19 # радиус сферы


x = 1

y = 2 # координаты заданной точки

z = 3

# вызов функции для вычисления расстояния между центром и заданной точкой

ans = check(cx, cy, cz, x, y, z);


# расстояние между центром и точкой меньше радиуса

if ans<(r**2):

    print("Point is inside the sphere")


# расстояние между центром и точкой равно радиусу

elif ans ==(r**2):

    print("Point lies on the sphere")


# расстояние между центром и точкой больше радиуса

else:

    print("Point is outside the sphere")
