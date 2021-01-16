import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height)) 

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

# FPS
clock = pygame.time.Clock()


# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/minchul/Desktop/python_game_project/pygame_basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/minchul/Desktop/python_game_project/pygame_basic/character.png")
#==>캐릭터는 움직여야함.
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) -(character_width/2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height -character_height #화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6


#이벤트루프가 실행되고 있어야 호출된 창이 꺼지지 않는다.
# 이벤트 루프
running = True # 게임이 진행중인가를 확인하는 변수
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정
    for event in pygame.event.get(): # 무조건 필요한 부분 키보드 마우스 움직임 확인함
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 확인
            running = False #while문 빠져나옴 ==> 게임이 진행중 아님

        if event.type == pygame.KEYDOWN: #키가 눌러졌을 때
            if event.key == pygame.K_LEFT: # 왼쪽방향키
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 오른쪽방향키
                to_x += character_speed
            elif event.key == pygame.K_UP: #위쪽 방향키
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: #아래쪽 방향키
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height


    screen.blit(background, (0,0)) #background변수에 담아놨던 이미지 불러옴. 두번째 인자 좌표값

    screen.blit(character, (character_x_pos,character_y_pos)) #캐릭터 그리기

    pygame.display.update() #매 프레임마다 다시 그려줌 (자바gui할때 쓰던 repaint랑 같은 개념인듯)


#pygame 종료
pygame.quit()