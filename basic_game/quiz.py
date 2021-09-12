import pygame
import random
#################################################################################
#################################################################################
#################################################################################
#################################################################################
#초기화
pygame.init()

#화면 크기
screen_width = 480      #가로
screen_height = 640     #세로
screen = pygame.display.set_mode((screen_width, screen_height))
#화면 타이틀 설정
pygame.display.set_caption("게임이름")     #게임이름

#FPS
clock = pygame.time.Clock()
#################################################################################
#################################################################################
#################################################################################
#################################################################################

#1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

#a. 배경화면 불러오기
background = pygame.image.load("C:\\Users\\82102\\Desktop\\2021-2\\Project\\game\\background.png")

#b. 캐릭터 불러오기
character = pygame.image.load("C:\\Users\\82102\\Desktop\\2021-2\\Project\\game\\character.png")
character_size = character.get_rect().size
character_width= character_size[0]              #가로크기
character_height = character_size[1]            #세로크기
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_height - character_height
character_speed = 0.3
to_x =0 #가로방향 이동크기
score = 0           #게임점수

#c. 똥 불러오기
enemy =pygame.image.load("C:\\Users\\82102\\Desktop\\2021-2\\Project\\game\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randrange(0, screen_width- enemy_width)
enemy_y_pos = 0
enemy_speed = 0.3

#d. 폰트 정의
game_font = pygame.font.Font(None, 40)      #폰트 객체 생성(글씨체, 크기)

#################################################################################
#################################################################################
#################################################################################
#################################################################################


#이벤트 루프
running = True
while running:      #화면이 꺼지지 바로 않도록
    dt = clock.tick(30)                     #게임화면의 초당 프레임 수 설정

    ######################################################################
    ######################################################################
    ######################################################################
    ######################################################################
    #2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():        #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:       #창이 닫히는 이벤트가 발생하였는가
            running = False                 #게임이 진행중이 아님
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            to_x = 0
    
    ######################################################################
    ######################################################################
    ######################################################################
    ######################################################################
    #3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    
    if character_x_pos<0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #똥의 이동, 점수 증가(5점)
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if enemy_rect.top <= screen_height - enemy_height:
        enemy_y_pos += enemy_speed * dt

    else:
        score = score + 5
        enemy_y_pos = 0
        enemy_x_pos = random.randrange(0, screen_width- enemy_width)
    
    ######################################################################
    ######################################################################
    ######################################################################
    ######################################################################
    #4. 충돌 처리

    #충돌 처리를 위한rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False
    
    ######################################################################
    ######################################################################
    ######################################################################
    ######################################################################
    #5. 화면에 그리기
    screen.blit(background, (0,0))

    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    score_show = game_font.render(str(score), True, (255,255,255))
    screen.blit(score_show, (10, 10))


    pygame.display.update()                                         #게임화면을 다시 그리기

#################################################################################
#################################################################################
#################################################################################
#################################################################################

#pygame 종료
pygame.quit()









