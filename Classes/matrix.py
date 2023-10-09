def summary(func):
    def wrapper(self):
        n = func(self)
        print(f"Summary equal to {n}")
    return wrapper

class Matrix():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.numbers = [[0 for _ in range(cols)] for _ in range(rows)]

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

    def setNumber(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.numbers[col][row] = value
        else:
            print("Given data is outside the matrix")

    def setNumbers(self, value):
        self.numbers = value

    def getNumber(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            print(self.numbers[col][row])
        else:
            print("Given data is outside the matrix")

    def showMatrix(self):
        print(f"matrix has {self.getCols()} columns and {self.getRows()} rows:")
        for row in self.numbers:
            print(row)

    def maxNumber(self):
        print(f"Biggest number in matrix - {max(max(row) for row in self.numbers)}")

    def minNumber(self):
        print(f"Smallest number in matrix - {min(min(row) for row in self.numbers)}")

    def getSumNumbers(self):
        sum = 0
        for row in self.numbers:
            for element in row:
                sum += element
        return sum

    @summary
    def showSumNumbers(self):
        return self.getSumNumbers()
