# decorator3.py

import time

def elapsed(func):
    def wrapper(*args, **kwargs):       # 일반 가변매개변수 , 키워드 가변매개변수 추가
       start = time.time()
       result = func(*args, **kwargs)   # 일반 가변매개변수 , 키워드 가변매개변수 추가
       end = time.time()
       print(f"함수 소요시간 : {end-start}초")
       return result
    return wrapper

@elapsed
def myfunc(msg, dic):
    print(f"{msg}, {dic}를 출력합니다.")

myfunc("You need Python", {1:'Python', 2:'js'})
myfunc("Error", {1:'Python', 2:'js'})