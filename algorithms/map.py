# Алгоритм на карте

# алгоритм бинарного поиска используется для сжатия координат точек
def bin_search(mass, target):
    if target < mass[0] or target >= mass[-1]:
        return -1
    left, right = 0, len(mass)
    while right - left > 1:
        mid = (right + left) // 2
        if mass[mid] > target:
            right = mid
        else:
            left = mid
    return left


# алгоритм строит массивы неповторяющихся координат Х и У для прямоугольников
# на основе этих массивов будет происходить сжатие координат для точек
# после этого создается пустая карта и заполняется прямоугольниками по принципу:
# сжатые координаты прямоугольников соответствуют индексу этих точек в заранее заготовленных массивах
def preprocessing(n):
    mas_rectangle = []
    points_x, points_y = set(), set()
    rec_file = open("../data/rectangles.txt", "r")
    for _ in range(n):
        points = [int(x) for x in rec_file.readline().split()]

        points_x.add(points[0])
        points_x.add(points[2])
        points_y.add(points[1])
        points_y.add(points[3])

        mas_rectangle.append(points)

    points_x, points_y = list(points_x), list(points_y)
    points_x.sort()
    points_y.sort()

    c_map = [[0] * (len(points_x) - 1) for _ in range(len(points_y) - 1)]

    for rec in mas_rectangle:
        compressed_x1 = points_x.index(rec[0])
        compressed_y1 = points_y.index(rec[1])
        compressed_x2 = points_x.index(rec[2])
        compressed_y2 = points_y.index(rec[3])

        for x in range(compressed_x1, compressed_x2):
            for y in range(compressed_y1, compressed_y2):
                c_map[len(points_y) - 2 - y][x] += 1
    return c_map, points_x, points_y


# для каждой точки вычисляем ее сжатые координаты с помощью бинарного поиска и
# возвращаем соответствующее значение карты по этим координатам
def algorithm(m, c_map, points_x, points_y):
    rec_file = open("../data/points.txt", "r")
    for _ in range(m):
        x, y = [int(x) for x in rec_file.readline().split()]

        compressed_x = bin_search(points_x, x)
        compressed_y = bin_search(points_y, y)

        if compressed_x == -1 or compressed_y == -1:
            print(0, end=" ")
        else:
            print(c_map[len(points_y) - 2 - compressed_y][compressed_x], end=" ")
