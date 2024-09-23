def matrix_chain_order(p):
    n = len(p)  # Количество матриц = длина массива размеров - 1
    m = [[0] * n for _ in range(n)]  # Таблица для хранения минимальных операций
    s = [[0] * n for _ in range(n)]  # Таблица для хранения индексов разбиения

    # m[i][i] = 0 для всех i, так как умножение одной матрицы не требует операций
    for i in range(n):
        m[i][i] = 0

    # l — длина цепочки матриц
    for l in range(2, n):  # Длина цепочки от 2 до n-1
        for i in range(n - l):  # Начало цепочки
            j = i + l - 1  # Конец цепочки
            m[i][j] = float('inf')
            for k in range(i, j):
                # q — стоимость умножения цепочек A_i...A_k и A_k+1...A_j
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    print_order(s, 0, n - 2)  # Исправлено на нулевую индексацию
    print()

    return m[0][n - 2]


def print_order(s, i, j):
    if i == j:
        print(f"A{i + 1}", end="")  # Коррекция индекса для вывода
    else:
        print("(", end="")
        print_order(s, i, s[i][j])
        print_order(s, s[i][j] + 1, j)
        print(")", end="")


if __name__ == "__main__":
    n = int(input("Введите количество матриц: "))  # Число матриц
    p = list(map(int, input("Введите размеры матриц: ").split()))  # Размеры матриц

    if len(p) != n + 1:
        print("Ошибка: количество введённых размеров должно быть равно количеству матриц + 1.")
    else:
        print(f"Минимальное количество умножений: {matrix_chain_order(p)}")
