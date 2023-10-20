import pygame as p
import random as r
import  math as m
from pygame import mixer as mi

p.init()
screen=p.display.set_mode((800,600))
condition = True

#title,icon and background
p.display.set_caption("SPACE ATTACK")
icon=p.image.load( "C:\\Users\\Ishit Dandawate\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\spaceman.png")
p.display.set_icon(icon)
background = p.image.load("C:\\ISHIT BACKUP\\2799006.jpg")

#player
player = p.image.load("C:\\ISHIT BACKUP\\001-space-shuttle.png")
playerx = 370
playery = 480

#enemy
enemyimg=[]
enemyx = []
enemyy = []
enemyxchange = []

#6 ENEMIES
for i in range(6):
    enemyimg.append(p.image.load("C:\\ISHIT BACKUP\\001-ghost.png"))
    enemyx.append(r.uniform(0, 650))
    enemyy.append(r.uniform(50, 150))
    enemyxchange.append(0.38)

#BULLET
bulletx=0
bullety=-1
bulletimg=p.image.load("C:\\ISHIT BACKUP\\001-bullet.png")
bulletstate="notready"

#SCORE DISPLAY
score = 0
font = p.font.Font('freesansbold.ttf', 32)
def renderscore():
    text = font.render("SCORE : " + str(score),True,(0,255,0))
    screen.blit(text,(0,0))

#ALL MUSICS
mi.music.load("C:\\ISHIT BACKUP\\super-mario-bros-4293.mp3")
mi.music.play(-1)
    

#GAMEOVER
playsound = True
crossy = 400        # GAME OVER LINE
font3 = p.font.Font('freesansbold.ttf', 35)
text3 = font3.render("-----",True,(255,255,255))
font4 = p.font.Font('freesansbold.ttf', 13)
text4 = font4.render("Game over",True,(0,25,25))

def gameover():
    global playsound
    mi.music.stop()
    gameoversound = mi.Sound("C:\\ISHIT BACKUP\\mixkit-sad-game-over-trombone-471.wav")
    if playsound:
        gameoversound.play()
        playsound = False
    font2 = p.font.Font('freesansbold.ttf', 100)
    text2 = font2.render("GAMEOVER",True,(255,0,0))
    screen.blit(text2,(140,250))
    
    
while condition:
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))

    for event in p.event.get():
        if event.type==p.QUIT:
            condition=False

        #PLAYER MOVEMENT
        if event.type == p.KEYDOWN:
            if event.key == p.K_RIGHT:
                if playerx>=744:
                    playerx=744
                else:
                    playerx += 50
            if event.key == p.K_LEFT:
                if playerx<=0:
                    playerx = 0
                else:
                    playerx -= 50
            if event.key == p.K_UP:
                if playery>0:
                    playery -= 25
                else:
                    playery=0
            if event.key == p.K_DOWN:
                if playery>=506:
                    playery=500
                if playery<600:
                    playery += 25
            if bullety<0:
                if event.key == p.K_SPACE:
                    bulletsound = mi.Sound("C:\\ISHIT PYTHON CODES\\ImpactBig8Bit GFX030903.mp3")
                    bulletsound.play()
                    bulletx=playerx+16
                    bullety=playery+14
                    bulletstate="fire"

    #ENEMY MOVEMENT
    for i in range(6):
        enemyx[i]+=enemyxchange[i]
        if enemyx[i] <= 0:
            enemyy[i]+=50
            enemyxchange[i] = 0.38
        if enemyx[i] >= 720:
            enemyy[i]+=50
            enemyxchange[i]=-0.38
        screen.blit(enemyimg[i], (enemyx[i], enemyy[i]))
        #COLLISION
        if m.sqrt(m.pow(enemyx[i]-bulletx,2)+m.pow(enemyy[i]-bullety,2)) <= 28:
            enemysound = mi.Sound("C:\\ISHIT BACKUP\\boom2.wav")
            enemysound.play()
            score+=1
            bullety=-1
            bulletstate="ready"
            enemyx[i]=r.uniform(0, 650)
            enemyy[i]=r.uniform(50, 150)

        # GAMEOVER CALL
        if enemyy[i]>=crossy or m.sqrt(m.pow(enemyx[i]-playerx,2)+m.pow(enemyy[i]-playery,2))<= 28:
            for j in range(6):
                enemyy[j]=1000
            gameover()
            break
    

    #BULLET
    if bulletstate=="fire":
        screen.blit(bulletimg,(bulletx,bullety))
        bullety-=0.7

    screen.blit(player, (playerx, playery))
    renderscore()
    screen.blit(text4,(0,crossy - 2))
    screen.blit(text3,(0,crossy))
    p.display.update()

