#generator.py

import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

list_job = [longtime_job() for i in range(5)]   # 리스트 컴프리헨션
print(list_job[0])   # 첫 번째 결과만 출력을 원했으나 for문 5번 모두 실행

print('====================================')

list_job2 = (longtime_job() for i in range(5))   # 제너레이터 표현식으로 변경
print(next(list_job2))   # 제너레이터 표현으로 만들어서 한번만 출력되게 해결