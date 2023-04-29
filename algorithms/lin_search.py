# Алгоритм перебора

# линейный алгоритм не требует подготовки
def preprocessing():
    return


# для каждой точки линейно проходимся по массиву прямоугольников и считаем, в сколько из них она включена
def algorithm(n, m):
    rec_file = open("../data/rectangles.txt", "r")
    mas_rectangle = [[int(x) for x in rec_file.readline().split()] for _ in range(n)]

    rec_file = open("../data/points.txt", "r")
    for _ in range(m):
        counter = 0
        point_x, point_y = [int(x) for x in rec_file.readline().split()]
        for rec in mas_rectangle:
            if rec[0] <= point_x < rec[2] and rec[1] <= point_y < rec[3]:
                counter += 1
        print(counter, end=" ")
