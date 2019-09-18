import pygame
import time
import random

pygame.init()

d_l=800
d_b=600
pygame.display.set_caption("SNAKE GAME")

screen=pygame.display.set_mode((d_l,d_b))

tempx=0
tempy=0
e=-1

score=0


w=(255,255,255)
b=(0,0,0)
r=(255,0,0)
g=(0,255,0)
blue=(0,0,255)
green=(24,175,55)
orange=(255,127,39)
p=(163,73,164)

block=20

head=[pygame.image.load("bleh1.png"),pygame.image.load("bleh2.png"),pygame.image.load("bleh3.png"),pygame.image.load("bleh4.png")]

apple=pygame.image.load("apple.png")
blood=pygame.image.load("blood.png")
boundaries=pygame.image.load("boundaries.png")
def snake(block,s_l,x):
    screen.blit(head[x], [s_l[-1][0],s_l[-1][1]])
    for i in s_l[:-1]:
        pygame.draw.rect(screen,blue,[i[0],i[1],block,block])

def scores(score,u,v,size):
    font=pygame.font.SysFont(None,size)
    textx=font.render("SCORE : " + str(score),True,p)
    screen.blit(textx,[u,v])

def highscore(score):
    try:
        high_score_file=open("highscore.txt","r")
        high_score=int(high_score_file.read())
        high_score_file.close()
        if high_score>score:
            font=pygame.font.SysFont(None,60)
            texty=font.render("HIGHSCORE : " +str(high_score),True,blue)
            screen.blit(texty,[300,180])
        else:
            font=pygame.font.SysFont(None,60)
            texty=font.render("HIGHSCORE : " + str(score),True,blue)
            screen.blit(texty,[300,180])
            high_score_file=open("highscore.txt","w")
            high_score_file.write(str(score))
            high_score_file.close()
    except IOError:
        font=pygame.font.SysFont(None,60)
        texty=font.render("HIGHSCORE : " +str(score),True,blue)
        screen.blit(texty,[300,180])
        high_score_file=open("highscore.txt","w")
        high_score_file.write(str(score))
        high_score_file.close()
        
            

def message(msg,color,p,q,size):
    font = pygame.font.SysFont(None,size)
    text=font.render(msg,True, color)
    screen.blit(text,[p,q])
##    pygame.display.update()

def gameloop():
    clock=pygame.time.Clock()

    x_change=0
    y_change=0

    score=0

    d=-1
    e=-1

    x=100
    y=100


    g_e=False
    g_o=False

    s_l=[]
    s_len=1

    applex=round(random.randrange(50, 700-block)/(block))*(block)
    appley=round(random.randrange(50, 500-block)/(block))*(block)

    
    while not g_e:
        while g_o==True:
            screen.fill(b)
            scores(score,350,100,60)
            highscore(score)
            message("YOU LOST.     PLAY AGAIN : P      EXIT GAME : E",r,50,300,45)
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_e:
                        pygame.quit()
                        quit()
                        screen.fill(b)
                        pygame.display.update()
                        g_e=True
                        g_o=False
                    elif event.key==pygame.K_p:
                        g_o=False
                        gameloop()
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()

                        
                    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                g_e=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-block
                    y_change=0
                    
                    d=1
                    
                elif event.key==pygame.K_RIGHT:
                    x_change=block
                    y_change=0
                    d=2
                    
                elif event.key==pygame.K_UP:
                    y_change=-block
                    x_change=0
                    d=3
                    
                elif event.key==pygame.K_DOWN:
                    y_change=block
                    x_change=0
                    d=4


        if x>700+block or x<0+50 or y>500+block or y<0+50:
            screen.blit(blood,[s_l[-1][0],s_l[-1][1]])
            pygame.display.update()
            time.sleep(2)
            g_o=True

        

        x+=x_change
        y+=y_change

        if x==applex and y==appley:
            applex=round(random.randrange(50, 700-block)/(block))*(block)
            appley=round(random.randrange(50, 500-block)/(block))*(block)
            s_len+=2
            score+=1
            
            
        s_h=[]
        s_h.append(x)
        s_h.append(y)
        s_l.append(s_h)
        s_lb=s_l[:-2]

        if len(s_l)>s_len:
            del s_l[0]
        screen.fill(b)
        screen.blit(boundaries,[50,50])
        scores(score,50,5,30)
##        pygame.draw.rect(screen,r,[applex,appley,block,block])
        screen.blit(apple,[applex,appley])
        
        if d==1:
            snake(block,s_l,3)
        elif d==2:
            snake(block,s_l,1)
        elif d==3:
            snake(block,s_l,0)
        elif d==4:
            snake(block,s_l,2)
        else:
            snake(block,s_l,0)

        if s_l[-1] in s_lb:
            screen.blit(blood,[s_l[-1][0],s_l[-1][1]])
            pygame.display.update()
            time.sleep(2)
            g_o=True

##        if tempx==s_l[0][0] and tempy==s_l[0][1]:
##            if e==1:
##                screen.blit(tail[3],[tempx,tempy])
##            if e==2:
##                screen.blit(tail[1],[tempx,tempy])
##            if e==3:
##                screen.blit(tail[0],[tempx,tempy])
##            if e==4:
##                screen.blit(tail[2],[tempx,tempy])
            
                
        pygame.display.update()

        clock.tick(15)


    pygame.quit()
    quit()

def snakegame():
    g_e=False
    while not g_e:
        screen.fill(b)
        message("SNAKE GAME",green,250,35,80)

        message("PLAY : P",orange,250,200,60)
        
        message("QUIT : E",orange,250,275,60)
        
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    screen.fill(b)
                    gameloop()
                elif event.key==pygame.K_e:
                    g_e=True
            elif event.type==pygame.QUIT:
                g_e=True
        
        pygame.display.update()
        
        

    pygame.quit()
    quit()
snakegame()

    
