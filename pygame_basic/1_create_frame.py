import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height)) 

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임 이름

#이벤트루프가 실행되고 있어야 호출된 창이 꺼지지 않는다.
# 이벤트 루프
running = True # 게임이 진행중인가를 확인하는 변수
while running:
    for event in pygame.event.get(): # 무조건 필요한 부분 키보드 마우스 움직임 확인함
        if event.type == pygame.QUIT: #창이 닫히는 이벤트 확인
            running = False #while문 빠져나옴 ==> 게임이 진행중 아님
#pygame 종료
pygame.quit()    