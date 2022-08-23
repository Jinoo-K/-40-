# pip install pygame

import pygame
import sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400

pygame.init()       # pygame 초기화
clock = pygame.time.Clock()     # clock 설정
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))       # 스크린 설정 600*400

def main():
    while True:
        for event in pygame.event.get():        # pygame의 event 불러오기
            if event.type == pygame.QUIT:       # X 버튼을 누르면 종료
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:        # spacebar를 누르면 space 출력
                if event.key == pygame.K_SPACE:
                    print("space")
        clock.tick(FPS)     # 위에 설정된 FPS로 동작
        screen.fill((255, 255, 255))
        
        pygame.display.update()     # 적용된 함수들 업데이트
        
if __name__ == "__main__" :
    main()