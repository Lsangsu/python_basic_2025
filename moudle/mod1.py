# mod1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b


if __name__=="__main__":   
    # 상위폴더에서 python mod1.py를 실행하면 if문 내 문장이 실행 / python -> import mod1 입력시 실행 X
    print(add(1, 4))
    print(sub(4, 2))




# 상단 Terminal - new terminal 활성화
# moudle 폴더로 이동 - cd moudle
# 파이썬 실행 - python
# mod1 모듈(mod1.py) 불러오기 - import mod1