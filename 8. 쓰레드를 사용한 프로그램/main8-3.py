import threading        # threading 모듈 불러오기

def sum(name, value):       # name과 value를 입력받아서 value 회수만큼 반복
    for i in range(0, value):
        print(f"{name} : {i}")
        
t1 = threading.Thread(target=sum, args=("1번 쓰레드", 10))      # name은 1번 쓰레드, value는 10
t2 = threading.Thread(target=sum, args=("2번 쓰레드", 10))      # name은 2번 쓰레드, value는 10

t1.start()      # 1,2번 쓰레드 시작
t2.start()

print("Main Thread")        # 메인 쓰레드 시작