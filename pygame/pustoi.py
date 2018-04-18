import pygame
from pygame import *
from math import pi,cos, sin

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
DISPLAY = (SCREEN_WIDTH,SCREEN_HEIGHT)
sky = (SCREEN_WIDTH,SCREEN_HEIGHT/2)		
grass = (SCREEN_WIDTH,SCREEN_HEIGHT/2)											 
pygame.init()	
screen = pygame.display.set_mode(DISPLAY)	
pygame.display.set_caption('Тюпов Артем ИУ7-22')		

a = 0
done = False

#Человек
man_WIDTH = 100                  
man_HEIGHT = 150                 
man_x = (SCREEN_WIDTH-man_WIDTH)//2
man_y = (SCREEN_HEIGHT-man_HEIGHT)//2

#Скейтбоард - доска
skateboard_1_WIDTH = 150
skateboard_1_HEIGHT = 30

#Скейтбоард - колесо - 1
skateboard_2_WIDTH = 1000
skateboard_2_HEIGHT = 1000
skateboard_2_x = 100
skateboard_2_y = 250
xc1 = 20
yc1 = 17
xc11 = 500
yc11 = 500
tetta = 0.5

sun_x = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
    #Фон
    bg1 = Surface(sky)	  
    bg1.fill(Color("lightblue"))  
    screen.blit(bg1, (0,0))
    bg2 = Surface(grass)
    bg2.fill(Color("green"))
    screen.blit(bg2, (0,500))


    #Скейтбоард - колесо - 1
    TRANSPARENT_COLOR = Color("#123456")
    skateboard_2 = Surface( (skateboard_2_WIDTH, skateboard_2_HEIGHT) )                                                                                  
    skateboard_2.set_colorkey(TRANSPARENT_COLOR)    
    skateboard_2.fill(TRANSPARENT_COLOR)

    pygame.draw.circle(skateboard_2, Color("brown"), (200, 200), 120, 0)
    pygame.draw.circle(skateboard_2, Color("yellow"), ( round(30*cos(a)+30*sin(a)+200),
    round(30*sin(a)-30*cos(a))+200), 10, 0)
    pygame.draw.circle(skateboard_2, Color("yellow"), ( round(30*cos(a+pi/2)+30*sin(a+pi/2)+200),
    round(30*sin(a+pi/2)-30*cos(a+pi/2))+200), 10, 0)
    pygame.draw.circle(skateboard_2, Color("red"), ( round(30*cos(a+5*pi/4)+30*sin(a+5*pi/4)+200),
    round(30*sin(a+5*pi/4)-30*cos(a+5*pi/4))+200), 10, 0)

    
    pygame.draw.polygon(skateboard_2, Color("blue"),
    ((round(6*cos(a+pi/4)+6*sin(a+pi/4)+200),round(6*sin(a+pi/4)-6*cos(a+pi/4))+200),
    (round(6*cos(a+pi)+6*sin(a+pi)+200),round(6*sin(a+pi)-6*cos(a+pi))+200),
    (round(6*cos(a+6*pi/2)+6*sin(a+3*pi/2)+200),round(6*sin(a+3*pi/2)-6*cos(a+3*pi/2))+200),0))

    
##    pygame.draw.line(skateboard_2, Color("black"), (8, 17), (32, 17),2)
##    pygame.draw.line(skateboard_2, Color("black"), (20, 17-12), (20, 17+12),2)
    screen.blit(skateboard_2, (skateboard_2_x,skateboard_2_y))

    # Солнце
    sun = Surface(DISPLAY)                                                                                  
    sun.set_colorkey(TRANSPARENT_COLOR)    
    sun.fill(TRANSPARENT_COLOR)
    pygame.draw.ellipse(sun, Color("yellow"),
                        Rect(0,50, 100,50), 0)
    screen.blit(sun, (sun_x,0))
    
    #Движение
    man_x += 2
    a += 0.04
    skateboard_2_x += 2
    sun_x += 2
    if sun_x >= 1000:
        sun_x = 0
    if man_x >= 1000:
        man_x = 0
        skateboard_2_x = 0
        skateboard_3_x = 0

    


    #отображаем все изменения на экране
    pygame.display.update()


# завершаем работу pman_ygame
pygame.quit()
