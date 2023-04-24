n = int(input("Введите кол-во экспонатов: "))
weight = [0] * (n+1)
price = [0] * (n+1)
for i in range(1, n+1):
    weight[i], price[i] = map(int, input("Вес и цена каждого экспоната: ").split())

m, k = map(int, input("Заходы и максимальный вес: ").split())

maxw = [[0] * (m * k + 1) for i in range(n + 1)]
for j in range(m*k+1):
    maxw[0][j] = 0

for i in range(1, n+1):
    for j in range(1, m*k+1):
        if weight[i] > j:
            maxw[i][j] = maxw[i - 1][j]
        else:
            maxw[i][j] = max(maxw[i - 1][j], maxw[i - 1][j - weight[i]] + price[i])

max_price = maxw[n][m * k]

stolen = []
j = m * k
for i in range(n, 0, -1):
    if maxw[i][j] != maxw[i - 1][j]:
        stolen.append(i)
        j -= weight[i]
        if j == 0:
            break

print("Максимальная сумма:", max_price)
print("Украденные экспонаты:", stolen)





