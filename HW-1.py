def transpose_matrix(matrix):
    # Определяем количество строк и столбцов в исходной матрице
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую матрицу с размерами, перевернутыми по отношению к исходной
    transposed = [[None for _ in range(rows)] for _ in range(cols)]

    # Заполняем новую матрицу значениями из исходной матрицы
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

# Пример использования функции
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)
