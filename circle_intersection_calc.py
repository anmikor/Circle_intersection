import random
import sys

def define_contact(obj1, obj2, N):
    x1, y1, r1 = obj1[0], obj1[1], obj1[2]
    x2, y2, r2 = obj2[0], obj2[1], obj2[2]
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**(0.5)
    square = 3.142 * (min(r1, r2)) ** 2
    radius_sum = (r1 + r2)
    if distance <= abs(r1 - r2):
        print(f'Окружности вписаны одна в другую, поэтому\n'
              f'площадь пересечения окружностей равна меньшей окружности: {round(square, 3)} кв. ед.')
    elif distance >= radius_sum:
        square = 0
        print(f'Окружности не пересекаются, площадь пересечения S = {square}\n'
              f'Расстояние между центрами равно {distance}\n'
              f'Сумма радиусов равна {radius_sum}')
    else:
        square_intersection(obj1, obj2, N)
        print(f'Площадь меньшей окружности  равна {round(square, 3)}')

def square_intersection(obj1: list, obj2: list, N: int):
    """
    random_x = x(center) - R + random(0, 2R)
    """
    x1, y1, r1 = obj1[0], obj1[1], obj1[2]
    x2, y2, r2 = obj2[0], obj2[1], obj2[2]
    NN = degree_list(N)
    square = []
    for number in NN:
        k = 0
        for point in range(1, number):
            random_x = x1 - r1 + random.uniform(0, 2*r1)
            random_y = y1 - r1 + random.uniform(0, 2*r1)
            distance1 = ((random_x - x1) ** 2 + (random_y - y1) ** 2) ** 0.5
            distance2 = ((random_x - x2) ** 2 + (random_y - y2) ** 2) ** 0.5
            if distance1 <= r1 and distance2 <= r2:
                k += 1
            else:
                continue
        print(k)
        relationship = k/number
        print(relationship)
        square.append(relationship*4*r1**2)
    result = zip(NN, square)
    for n, S in result:
        print(f'При N = {n} бросков площадь пересечения равна {round(S, 3)}')

def degree_list(N: int):
    NN = []
    for degree in list(range(0, 4)):
        n = N * 10 ** degree
        NN.append(n)
    print(NN)
    return NN



if __name__ == "__main__":

    try:
        circle1 = list(map(float, input("Введите параметры 1-й окружности x1 y1 r1 через пробел : ").strip().split()))[:3]
        print("x1,y1,r1 - ", circle1)
    except ValueError:
        print('Число введено с ошибкой!  Запустите программу заново!')
        sys.exit(0)
    try:
        circle2 = list(map(float, input("Введите параметры 2-й окружности x2 y2 r2 через пробел : ").strip().split()))[:3]
        print("x2,y2,r2 - ", circle2)
    except ValueError:
        print('Число введено с ошибкой!  Запустите программу заново!')
        sys.exit(0)
    if len(circle1) != 3 or len(circle2) != 3:
        print('Введено недостаточно чисел! Запустите программу заново!')
        sys.exit(0)
    try:
        N = int(input("Введите начальное число точек N (не больше 200): "))
    except ValueError:
        print('Число введено с ошибкой!  Запустите программу заново!')
        sys.exit(0)
    if N > 200:
        print('Введите меньшее начальное число N - ограничение по времени работы программы')
    else:
        define_contact(circle1, circle2, N)






# r1 = float(input('радиус 1-й окружности: '))
# x1 = float(input('координата x 1-й окружности: '))
# y1 = float(input('координата y 1-й окружности: '))
# r2 = float(input('радиус 2-й окружности: '))
# x2 = float(input('координата x 2-й окружности: '))
# y2 = float(input('координата y 2-й окружности: '))

# print(r1)