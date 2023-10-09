import random
from Classes.matrix import Matrix
from Classes.sort import Sort

#Створити клас – матриця, який містить двовимірний масив для зберігання її елементів, кількість рядків та стовпців.
#Визначити конструктор, функції для зміни та виведення елементів матриці, пошуку мінімального та максимального елементів,
#обчислення суми елементів матриці. Відсортувати масив екземплярів класу матриць за зростанням суми елементів з використанням алгоритму сортування вибором.

def generateRandomMatrix(cols, rows):
    return [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

matrixArray = []
for _ in range(5):
    rows = random.randint(1, 5)
    cols = random.randint(1, 5)
    randomMatrix = Matrix(cols, rows)
    randomMatrix.setNumbers(generateRandomMatrix(cols, rows))
    matrixArray.append(randomMatrix)
    randomMatrix.minNumber()
    randomMatrix.maxNumber()

sorter = Sort(matrixArray)
sorter.showAllMatrix()

print("\nBefore sort:")
sorter.showMatricesSum()

print("\nAfter sort:")
sorter.selectionSort()