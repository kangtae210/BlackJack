import pygame
import os
#################################################################################
#초기화
pygame.init()

#화면 크기
screen_width = 640      #가로
screen_height = 480     #세로
screen = pygame.display.set_mode((screen_width, screen_height))
#화면 타이틀 설정
pygame.display.set_caption("NADO PANG")     #게임이름

#FPS
clock = pygame.time.Clock()
#################################################################################

#1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__)            #현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")   #이미지 폴더 위치

#배경
background = pygame.image.load(os.path.join(image_path, "background.png"))
#스테이지
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]    #스테이지의 높이 위에 캐릭터를 두기 위해 사용

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width= character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos =screen_height - character_height - stage_height
character_to_x = 0
character_speed = 0.2

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size= weapon.get_rect().size
weapon_width = weapon_size[0]
#무기 여러개 발사 가능
weapons = []
#무기 이동속도
weapon_speed = 10

#공 만들기(4개 크기에 대하여 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "ballon1.png")),
    pygame.image.load(os.path.join(image_path, "ballon2.png")),
    pygame.image.load(os.path.join(image_path, "ballon3.png")),
    pygame.image.load(os.path.join(image_path, "ballon4.png"))

]
#공 크기에 따른 최초 스피드
ball_speed_y =[-18, -15, -12, 9]

#공들
balls = []
balls.append({
    "pos_x" : 50,                            #공의 좌표.
    "pos_y" : 50,                   
    "img_idx" : 0,                       #공의 이미지 인덱스
    "to_x" : 3,                              #공의 x,y축 이동방향
    "to_y" : -6,    
    "init_spd_y" : ball_speed_y[0]          #y 최초 속도
})


#이벤트 루프
running = True
while running:      #화면이 꺼지지 바로 않도록
    dt = clock.tick(30)                     #게임화면의 초당 프레임 수 설정


    #2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():        #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:       #창이 닫히는 이벤트가 발생하였는가
            running = False                 #게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                character_to_x += character_speed  
            if event.key == pygame.K_SPACE:         #무기발사
                weapon_x_pos = character_x_pos + character_width/2- weapon_width/2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
        
  

        
    #3. 게임 캐릭터 위치 정의
    if character_x_pos <0:
        character_x_pos = 0
    if character_x_pos>screen_width - character_width:
        character_x_pos = screen_width - character_width
    character_x_pos += character_to_x  * dt

    #무기 위치 조정

    weapons = [  [w[0], w[1] - weapon_speed]   for w in weapons]  #무기 위치를 위로 올림
    weapons = [  [w[0], w[1]               ] for w in weapons if w[1]>0 ]  
    

    #공의 위치 조정
    for ball_index, ball_value in enumerate(balls):
        ball_pos_x = ball_value["pos_x"]      
        ball_pos_y = ball_value["pos_y"]
        ball_img_idx = ball_value["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

    #가로벽에 닿았을 때 공 이동방향 변경(벽에 튕겨 나오기)
    if ball_pos_x <0 or ball_pos_x >screen_width - ball_width:
        ball_value["to_x"] = ball_value["to_x"] * (-1)

    #세로방향 이동
    if ball_pos_y >= screen_height - stage_height - ball_height:    #스테이지에 튕김처리
        ball_value["to_y"] = ball_value["init_spd_y"]
    else:                                                           #포물선처럼 이동
        ball_value["to_y"] += 0.5
  
    
    ball_value["pos_x"] += ball_value["to_x"]
    ball_value["pos_y"] += ball_value["to_y"]
 
  
  
  
  
  
  
  
  
  
  
    #4. 충돌 처리

    #4. 화면에 그리기
    screen.blit(background, (0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_x"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))


    screen.blit(stage, (0,screen_height-stage_height))
    screen.blit(character, (character_x_pos , character_y_pos))



    pygame.display.update()                                         #게임화면을 다시 그리기


#pygame 종료
pygame.quit()


























