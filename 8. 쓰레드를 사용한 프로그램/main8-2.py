import threading        # threading 모듈 불러오기
import time         # time 모듈 불러오기

def thread_1() :        # thread_1 함수로 1초마다 쓰레드1 동작을 출력
    while True :
        print("쓰레드1 동작")
        time.sleep(1.0)
        
t1 = threading.Thread(target=thread_1)      # 쓰레드 설정
t1.daemon = True        # 쓰레드를 데몬쓰레드로 설정하여 메인동작이 실행될 때만 실행
t1.start()      # 쓰레드 시작

while True:         # 메인 동작을 2초마다 출력
    print("메인 동작")
    time.sleep(2.0)