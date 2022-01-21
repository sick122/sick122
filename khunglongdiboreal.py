from posixpath import supports_unicode_filenames
import pgzrun
from pygame import Color
from pgzhelper import *


WITDH=800
HEIGHT=600

background=Actor('background')
runner=Actor('run1')
run_images=['run1','run2','run3','run4','run5','run6','run7','run8']
runner.images=run_images
runner.x=100
runner.y=450

velocity_y=0
gravity=1

obstacels_timeout=0
obstacels=[]

score =0
game_over=False



def update():
    global velocity_y , gravity , obstacels_timeout , score, game_over , obstacels 
    runner.next_image()

    obstacels_timeout+=1
    if obstacels_timeout > 50:
        actor=Actor('catus')
        actor.x=800
        actor.y=450
        obstacels.append(actor)
        obstacels_timeout=0
    for actor in obstacels :
        actor.x-=8
        if actor.x<-50:
            score=score+1
            obstacels.remove(actor)
    if runner.collidelist(obstacels)!=-1:
        game_over=True
        obstacels.remove(actor)
        sounds.gameover.play()



    if keyboard.up and runner.y==450 :
        velocity_y=-20
        sounds.impact.play()
    runner.y+=velocity_y
    velocity_y+=gravity
    if runner.y>450:
        velocity_y=0
        runner.y=450
    if keyboard.space:
        game_over= False
        score=0
        obstacels=[]



def draw():
    background.draw()
    
    if game_over:
        screen.draw.text('Game Over',(300,300),color=(255,255,255),fontsize=60)
        screen.draw.text('Final score:'+str(score),(305,360),color=(255,0,255),fontsize=80)
        screen.draw.text('Press space to restart',(305,400),color=(100,100,255),fontsize=60)
    else:
        screen.draw.text('Score:'+str(score),(10,15),color=(255,0,255),fontsize=30)
        runner.draw()
        for actor in obstacels:
            actor.draw()
pgzrun.go()
