"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).

Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

Выполнено Салтыковой Екатериной
04.08.20
"""


class Matrix:

    # формирование матрицы
    def __init__(self, matrix_data: list):
        self.matrix = matrix_data

    def __str__(self):
        result = ''
        for row in self.matrix:
            result += ' '.join(str(el) for el in row) + '\n'
        return result

    def __add__(self, other):
        new_matrix = []
        for i in range(0, len(self.matrix)):
            tem_list = [self.matrix[i][j] + other[i][j] for j in range(0, len(self.matrix[i]))]
            new_matrix.append(tem_list)
        return Matrix(new_matrix)

    def __getitem__(self, item):
        return self.matrix[item]


matrix_1 = Matrix([[1, 2, 3], [1, 4, 5]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6]])

print(matrix_1 + matrix_2)
print(matrix_1)



