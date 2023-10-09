from Classes.matrix import Matrix

class Sort(Matrix):
    def __init__(self, array):
        self.matrixArray = array

    def showMatrixByIndex(self, i):
        if 0 <= i < len(self.matrixArray):
            matrix = self.matrixArray[i]
            matrix.showMatrix()
        else:
            print("No matrix under that index.")

    def showAllMatrix(self):
        for i, matrix in enumerate(self.matrixArray):
            self.showMatrixByIndex(i)

    def showMatricesSum(self):
        n = 0
        for matrix in self.matrixArray:
            n += 1
            print(f"{n}st martix sum is {matrix.getSumNumbers()}")

    def selectionSort(self):
        for i in range(len(self.matrixArray) - 1):
            minIndex = i
            for j in range(i + 1, len(self.matrixArray)):
                jSum = self.matrixArray[j].getSumNumbers()
                minIndexSum = self.matrixArray[minIndex].getSumNumbers()
                if jSum < minIndexSum:
                    minIndex = j
            self.matrixArray[i], self.matrixArray[minIndex] = self.matrixArray[minIndex], self.matrixArray[i]
        self.showMatricesSum()