# game/__init__.py
from .graphic.render import render_test    # 패키지 내 모듈을 미로 불러오기
# from .sound.echo import echo_test


VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")


# 패키지 초기화 코드 작성
# 초기화 코드는 한 번 실행된 후에는 다시 import해도 실행되지 않음!
print("Initializing game...")