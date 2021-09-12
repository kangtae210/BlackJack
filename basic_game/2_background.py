import pygame

#초기화
pygame.init()

#화면 크기
screen_width = 480      #가로
screen_height = 640     #세로

screen = pygame.display.set_mode((screen_width, screen_height))
#화면 타이틀 설정
pygame.display.set_caption("NADO game")     #게임이름

#배경이미지
background = pygame.image.load("C:\\Users\\82102\\Desktop\\2021-2\\Project\\game\\background.png")

#이벤트 루프
running = True
while running:      #화면이 꺼지지 바로 않도록
    for event in pygame.event.get():        #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:       #창이 닫히는 이벤트가 발생하였는가
            running = False                 #게임이 진행중이 아님
    screen.blit(background, (0,0))          #배경그리기
    pygame.display.update()                 #게임화면을 다시 그리기

#pygame 종료
pygame.quit()


























