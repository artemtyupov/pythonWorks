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

#Скейтбоард - колесо - 1
skateboard_2_WIDTH = 48
skateboard_2_HEIGHT = 48
skateboard_2_x = (SCREEN_WIDTH-95)//2
skateboard_2_y = (SCREEN_WIDTH+90)//2

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

    pygame.draw.circle(skateboard_2, Color("brown"), (20, 17), 12, 0)

    pygame.draw.line(skateboard_2,Color("red"),( round(7*cos(a)+7*sin(a)+20),
    round(7*sin(a)-7*cos(a))+17),(round(7*cos(a+pi) + 7*sin(a+pi)+20), round(7*sin(a+pi)-7*cos(a+pi))+17), 2)
    
    pygame.draw.line(skateboard_2,Color("red"),( round(7*cos(a+pi/2)+7*sin(a+pi/2)+20),
    round(7*sin(a+pi/2)-7*cos(a+pi/2))+17),(round(7*cos(1.5*pi+a) + 7*sin(1.5*pi+a)+20), round(7*sin(1.5*pi+a)-7*cos(1.5*pi+a))+17), 2)
    
    screen.blit(skateboard_2, (skateboard_2_x,skateboard_2_y))

    
    #Движение
    a += 0.04
    skateboard_2_x += 0.5



    #отображаем все изменения на экране
    pygame.display.update()


# завершаем работу pman_ygame
pygame.quit()
