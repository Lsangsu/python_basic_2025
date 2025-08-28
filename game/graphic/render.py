#render.py

# from game.sound.echo import echo_test  # 절대경로
from ..sound.echo import echo_test       # 상대경로


def render_test():
    print("render")
    echo_test()