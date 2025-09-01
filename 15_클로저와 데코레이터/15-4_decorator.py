# decorator.py

import time

def myfunc():
    start = time.time()
    print("함수가 실행됩니다.")
    end = time.time()
    print(f"함수 소요시간 : {end-start}초")

myfunc()

print('==============================================')

def elapsed(func):             #elasped=경과
    def wrapper():
       start = time.time()
       result = func()
       end = time.time()
       print(f"함수 소요시간 : {end-start}초")
       return result
    return wrapper

def myfunc2():
    print("함수가 실행됩니다.")

elapsed(myfunc2)()