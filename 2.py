def multiplication(size, i, j):
    if j - i <= 1:
        return 0

    min_Size = 10 ** 10

    for k in range(i + 1, j):
        now_Size = multiplication(size, i, k) + multiplication(size, k, j) + size[i] * size[k] * size[j]
        min_Size = min(min_Size, now_Size)

    return min_Size


print('Количество операций:', multiplication([20, 60, 10, 120], 0, 3))





