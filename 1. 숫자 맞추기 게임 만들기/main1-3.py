import random # 랜덤 모듈 불러오기

random_number = random.randint(1, 100) # 1~100 사이 임의의 수 생성

# print(random_number) # 출력

game_count = 1 # 게임 카운트 최초 1회

while True : # while 반복문 (계속 반복)
    try : # try 문으로 에러 발생하지 않았을 때 작동
        my_number = int(input("1 ~ 100 사이의 숫자를 입력하세요 : "))
        
        if my_number > random_number : # 입력값이 임의값보다 크면 다운
            print("다운")
        elif my_number < random_number : # 입력값이 임의값보다 작으면 업
            print("업")
        elif my_number == random_number : # 입력값이 임의값과 같을 때
            print(f"축하합니다. {game_count}회 만에 맞췄습니다.") # f-string
            break # 반복문 탈출
        
        game_count += 1 # 게임 카운트
    
    except : # 에러 발생시 출력
        print("에러가 발생했습니다. 숫자를 입력하세요")
