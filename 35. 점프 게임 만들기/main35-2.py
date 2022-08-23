# pip install pygame

import pygame
import sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400

pygame.init()       # pygame 초기화
clock = pygame.time.Clock()     # clock 설정
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))       # 스크린 설정 600*400

class Player():     # Player Class 생성
    def __init__(self, x, y) :      # 객체 생성 시 초기화
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10
        
    def draw(self) :        # 파란색 네모 40*40 사이즈 생성
        return pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, 40, 40))
    
    def jump(self) :        # Player 점프 구현
        if self.isJump:
            if self.jumpCount >= -10 :
                neg = 1
                if self.jumpCount < 0 :
                    neg = -1
                self.y -= self.jumpCount**2 * 0.7 * neg
                self.jumpCount -= 1
            else :
                self.isJump = False
                self.jumpCount = 10
                
player = Player(50, MAX_HEIGHT - 40)        # player로 객체 생성

def main():
    while True:
        for event in pygame.event.get():        # pygame의 event 불러오기
            if event.type == pygame.QUIT:       # X 버튼을 누르면 종료
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_SPACE:
                    player.isJump = True        # spacebar를 누르면 player 점프
                    
        clock.tick(FPS)     # 위에 설정된 FPS로 동작
        screen.fill((255, 255, 255))
        
        player_rect = player.draw()
        player.jump()
        
        print(player_rect)
        
        pygame.display.update()     # 적용된 함수들 업데이트
        
if __name__ == "__main__" :
    main()