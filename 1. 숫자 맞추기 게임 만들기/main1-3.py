import random # 랜덤 모듈 불러오기

random_number = random.randint(1, 100)

game_count = 1

while True :
    try : # try 문으로 에러 발생하지 않았을 때 작동
        my_number = int(input("1 ~ 100 사이의 숫자를 입력하세요 : "))
        
        if my_number > random_number :
            print("다운")
        elif my_number < random_number :
            print("업")
        elif my_number == random_number :
            print(f"축하합니다. {game_count}회 만에 맞췄습니다.")   # f-string
            break
        
        game_count += 1
    
    except : # 에러 발생시 출력
        print("에러가 발생했습니다. 숫자를 입력하세요")
