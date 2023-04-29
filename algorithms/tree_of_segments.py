# Алгоритм на дереве

# узел дерева, включает в себя значение,
# границы отрезка, за который он отвечает (правая граница не включена)
# и ссылки на детей
class Node:
    def __init__(self, left=None, right=None):
        self.left_border, self.right_border = left, right
        self.left_child, self.right_child = None, None
        self.value = 0


# рекурсивная функция создает дерево для заданного отрезка
def create_tree(left, right):
    node = Node(left, right)
    if left + 1 < right:
        mid = (right + left) // 2
        node.left_child = create_tree(left, mid)
        node.right_child = create_tree(mid, right)
    return node


# функция используется для копирования узла дерева без копирования детей
def copy_without_children(node):
    new_node = Node(node.left_border, node.right_border)
    new_node.value = node.value
    return new_node


# функция используется для копирования узла дерева с изменением значения и с сохранением ссылок на старых детей
def copy_of_node(node, v):
    new_node = Node(node.left_border, node.right_border)
    new_node.value = node.value + v
    new_node.left_child = node.left_child
    new_node.right_child = node.right_child
    return new_node


# функция используется для создания новой версии дерева
def change_tree(node, left, right, value):
    if left <= node.left_border and node.right_border <= right:
        return copy_of_node(node, value)
    if right <= node.left_border or node.right_border <= left:
        return node
    new_node = copy_without_children(node)
    new_node.left_child = change_tree(node.left_child, left, right, value)
    new_node.right_child = change_tree(node.right_child, left, right, value)
    return new_node


# функция проходится по дереву и считает количество прямоугольников, в которые входит точка
def find(node, target):
    if not node.right_child and not node.left_child:
        return node.value
    mid = (node.right_border + node.left_border) // 2
    if target < mid:
        return node.value + find(node.left_child, target)
    return node.value + find(node.right_child, target)


# алгоритм бинарного поиска используется для сжатия координат точек
def bin_search(mass, target):
    if target < mass[0] or target > mass[-1]:
        return -1
    left, right = 0, len(mass)
    while right - left > 1:
        mid = (right + left) // 2
        if mass[mid] >= target:
            right = mid
        else:
            left = mid
    if mass[right] == target:
        return right
    return left


# алгоритм строит массивы неповторяющихся координат Х и У для прямоугольников
# на основе этих массивов будет происходить сжатие координат для точек
# после этого создается дерево отрезков по принципу:
# создается новая версия дерева для каждого У являющегося границей прямоугольника,
# в эту версию дерева сохраняются изменения по оси Х
def preprocessing(n):
    if n:
        rec_file = open("../data/rectangles.txt", "r")
        mas_x_changes = []
        points_x, points_y = set(), set()
        for _ in range(n):
            points = [int(x) for x in rec_file.readline().split()]

            points_x.add(points[0])
            points_x.add(points[2])
            points_y.add(points[1])
            points_y.add(points[3])

            mas_x_changes.append([points[1], points[0], points[2], 1])
            mas_x_changes.append([points[3], points[0], points[2], -1])

        points_x, points_y = list(points_x), list(points_y)
        points_x.sort()
        points_y.sort()
        mas_x_changes = sorted(mas_x_changes, key=lambda x: x[0])

        tree = create_tree(0, len(points_x) - 1)
        persistent_trees = [tree]
        new_tree = None

        pref, ind = mas_x_changes[0][0], 0
        while ind <= len(mas_x_changes) - 1:
            if mas_x_changes[ind][0] != pref:
                persistent_trees.append(new_tree)
                pref = mas_x_changes[ind][0]

            while ind != len(mas_x_changes) and pref == mas_x_changes[ind][0]:
                new_tree = change_tree(persistent_trees[-1] if not new_tree else new_tree,
                                       points_x.index(mas_x_changes[ind][1]), points_x.index(mas_x_changes[ind][2]),
                                       mas_x_changes[ind][3])
                ind += 1

        persistent_trees.append(tree)
        return persistent_trees, points_x, points_y
    return False, False, False


# для каждой точки вычисляем ее сжатые координаты с помощью бинарного поиска и
# проходимся по нужной версии дерева и возвращаем количество прямоугольников, в которые входит точка
def algorithm(m, persistent_trees, points_x, points_y):
    rec_file = open("../data/points.txt", "r")
    if persistent_trees is not False:
        for _ in range(m):
            x, y = [int(x) for x in rec_file.readline().split()]

            compressed_x = bin_search(points_x, x)
            compressed_y = bin_search(points_y, y)

            if compressed_x == -1 or compressed_y == -1:
                print(0, end=" ")
            else:
                print(find(persistent_trees[compressed_y + 1], compressed_x), end=" ")
    else:
        for _ in range(m):
            x, y = [int(x) for x in input().split()]

            print(0, end=" ")
