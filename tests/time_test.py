from time import perf_counter
from algorithms import lin_search, map, tree_of_segments


# функция генерирует тестовый набор прямоугольников вложенных друг-в-друга с координатами с шагом больше 1
def create_rectangles(number):
    rec_file = open("../data/rectangles.txt", "w")
    for i in range(number):
        rec_file.write(str(10 * i) + " " + str(10 * i) + " " + str(10 * (2 * number - i)) +
                       " " + str(10 * (2 * number - i)) + "\n")


# функция генерирует неслучайный набор точек
# распределенных более-менее равномерно по ненулевому пересечению прямоугольников
def create_points(number):
    points_file = open("../data/points.txt", "w")
    for i in range(number):
        points_file.write(str(pow(1009 * i, 31) % (20 * number)) + " " + str(pow(1013 * i, 31) % (20 * number)) + "\n")


# функция считает среднее время подготовки для работы линейного алгоритма для разного набора прямоугольников
def test_lin_alg_prep():
    for i in range(13):
        create_rectangles(2 ** i)
        time_sum = 0
        for x in range(10):
            begin = float(perf_counter())
            lin_search.preprocessing()
            time_sum += float(perf_counter()) - begin
        time_sum /= 10
        print(2 ** i, time_sum)


# функция считает среднее время работы линейного алгоритма для разного набора прямоугольников
def test_lin_alg():
    for i in range(13):
        create_rectangles(2 ** i)
        time_sum = 0
        for x in range(10):
            begin = float(perf_counter())
            lin_search.algorithm(2 ** i, 100000)
            time_sum += float(perf_counter()) - begin
        time_sum /= 10
        print(2 ** i, time_sum)


# функция считает среднее время подготовки для работы алгоритма на карте для разного набора прямоугольников
def test_map_ald_prep():
    for i in range(13):
        create_rectangles(2 ** i)
        time_sum = 0
        for x in range(10):
            begin = float(perf_counter())
            map.preprocessing(2 ** i)
            time_sum += float(perf_counter()) - begin
        time_sum /= 10
        print(2 ** i, time_sum)


# функция считает среднее время работы алгоритма на карте для разного набора прямоугольников
def test_map_alg():
    for i in range(13):
        create_rectangles(2 ** i)
        time_sum = 0
        for x in range(10):
            c_map, points_x, points_y = map.preprocessing(2 ** i)
            begin = float(perf_counter())
            map.algorithm(100000, c_map, points_x, points_y)
            time_sum += float(perf_counter()) - begin
        time_sum /= 10
        print(2 ** i, time_sum)


# функция считает среднее время подготовки для работы алгоритма на дереве отрезков для разного набора прямоугольников
def test_tree_ald_prep():
    for i in range(13):
        create_rectangles(2 ** i)
        time_sum = 0
        for x in range(10):
            begin = float(perf_counter())
            tree_of_segments.preprocessing(2 ** i)
            time_sum += float(perf_counter()) - begin
        time_sum /= 10
        print(2 ** i, time_sum)


# функция считает среднее время работы алгоритма на дереве отрезков для разного набора прямоугольников
def test_tree_alg():
    for i in range(13):
        create_rectangles(2 ** i)
        time_sum = 0
        for x in range(10):
            t_map, points_x, points_y = tree_of_segments.preprocessing(2 ** i)
            begin = float(perf_counter())
            tree_of_segments.algorithm(100000, t_map, points_x, points_y)
            time_sum += float(perf_counter()) - begin
        time_sum /= 10
        print(2 ** i, time_sum)


test_tree_alg()