import pygame

#초기화
pygame.init()

#화면 크기
screen_width = 480      #가로
screen_height = 640     #세로
pygame.display.set_mode((screen_width, screen_height))
#화면 타이틀 설정
pygame.display.set_caption("NADO game")

#이벤트 루프
running = True
while running:      #화면이 꺼지지 바로 않도록
    for event in pygame.event.get():        #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:       #창이 닫히는 이벤트가 발생하였는가
            running = False                 #게임이 진행중이 아님


#pygame 종료
pygame.quit()