import random

n = int(input('Введите число элементов списка: '))
array = []
for _ in range(n):
    array.append(random.randint(-100, 100))
answer = answer1 = 1

for i in range(n - 1):
    if array[i + 1] > array[i]:
        answer1 += 1
    else:
        answer = max(answer, answer1)
        demoAnswer = 1

print(array, 'Длина максимальной последовательности:', answer)




