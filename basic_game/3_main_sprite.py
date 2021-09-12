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


#스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:\\Users\\82102\\Desktop\\2021-2\\Project\\game\\character.png")
character_size = character.get_rect().size              #이미지의 크기 구하기
character_width = character_size[0]                     #캐릭터의 가로 크기
character_height = character_size[1]                    # 캐릭터의 세로 크기

character_x_pos = (screen_width/2) - (character_width/2) #화면가로의 절반크기에 해당하는 곳에 위치
character_y_pos = screen_height   - character_height    #화면세로의 가장 아래에 해당하는 곳에 위치


#이벤트 루프
running = True
while running:      #화면이 꺼지지 바로 않도록
    for event in pygame.event.get():        #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:       #창이 닫히는 이벤트가 발생하였는가
            running = False                 #게임이 진행중이 아님
    screen.blit(background, (0,0))          #배경그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()                 #게임화면을 다시 그리기










#pygame 종료
pygame.quit()


























