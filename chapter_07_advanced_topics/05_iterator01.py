# iterator를 Class로 구현하기
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0

    # __iter__ method > iterable object
    def __iter__(self):
        return self

    # __next__ method > iterable 객체의 값을 차례대로 반환    
    def __next__(self):
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result
    
# 역순으로 지정하는 iterator
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data) - 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position < 0: raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result
    
if __name__ == "__main__":
    name_list = ["amy", "john", "ken"]
    iter = MyIterator(name_list)
    for name in iter:
        print(name)

    reversed_iter = ReverseIterator(name_list)
    for name in reversed_iter:
        print(name)