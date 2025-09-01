# iterator.py

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0

    def __iter__(self):   # 반복 가능학 객체를 이터레이터 객체로 변환
        return self
    
    def __next__(self):   # 이터레이터로 변화한 객체의 값을 차례대로 반환
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result
    
if __name__ == '__main__':
    list = MyIterator([1, 2, 3])
    for i in list:
        print(i)