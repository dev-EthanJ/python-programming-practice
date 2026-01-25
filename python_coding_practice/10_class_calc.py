class Calculator:
    def __init__(self, data):
        self.data = data
        self.sum_data = None
        self.avg_data = None

    def sum(self):
        if self.sum_data is None:
            sum_total = 0
            for i in self.data:
                sum_total += i
            self.sum_data = sum_total
        return self.sum_data 
    
    def avg(self):
        if self.sum_data is None:
            self.sum()
        self.avg_data = self.sum_data / len(self.data)
        return self.avg_data 


if __name__ == "__main__":
    cal1 = Calculator([1, 2, 3, 4, 5])
    print(cal1.sum())
    print(cal1.avg())
    cal2 = Calculator([6, 7, 8, 9, 10])
    print(cal2.sum())
    print(cal2.avg())