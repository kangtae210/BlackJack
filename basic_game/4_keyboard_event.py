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

#이동할 좌표
to_x = 0
to_y = 0

#이벤트 루프
running = True
while running:      #화면이 꺼지지 바로 않도록
    for event in pygame.event.get():        #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:       #창이 닫히는 이벤트가 발생하였는가
            running = False                 #게임이 진행중이 아님
        
        if event.type == pygame.KEYDOWN:    #키가 눌렸는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 1                   
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1                   
            elif event.key == pygame.K_DOWN:
                to_y += 1           
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x
    character_y_pos += to_y
    
    #캐릭터가 화면 밖으로 벗어나지 않도록 조정
    if character_x_pos<0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    if character_y_pos<0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height        
    
    screen.blit(background, (0,0))          #배경그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()                 #게임화면을 다시 그리기










#pygame 종료
pygame.quit()


























