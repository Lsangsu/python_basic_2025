# reviterator.py
# 입력한 데이터를 역순으로 출력하기

class RevIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data)-1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result
    
if __name__ == '__main__':
    list = RevIterator([1, 2, 3])
    for i in list:
        print(i)