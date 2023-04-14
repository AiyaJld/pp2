import pygame as pg
import os

pg.init()

screen = pg.display.set_mode((800, 600))
BACKGROUND = pg.image.load('assets\\bckg3.png').convert()
BACKGROUND = pg.transform.scale(BACKGROUND, (800, 600))
screen.blit(BACKGROUND, (0, 0))
is_playing = True

sound_files = os.listdir('music\\')
sound_images = os.listdir('assets\\sound_image\\')
play_images = os.listdir('assets\\play_image\\')
sound_images.sort()
sound_files.sort()
play_images.sort()
sound_queue = []
for filename in sound_files:
    sound = pg.mixer.Sound('music\\' + filename)
    sound_queue.append(sound)
music_index = 0
play_index = 1
sound_queue[music_index].play()

def chagneSoundsImage():
    SOUND_IMAGE = pg.image.load('assets\\sound_image\\' + sound_images[music_index]).convert()
    SOUND_IMAGE = pg.transform.scale(SOUND_IMAGE, (300, 315))
    screen.blit(SOUND_IMAGE, (240, 36))

def changePlay():
    PLAY_IMAGE = pg.image.load('assets\\play_image\\' + play_images[play_index]).convert()
    PLAY_IMAGE = pg.transform.scale(PLAY_IMAGE, (45, 50))
    screen.blit(PLAY_IMAGE, (370, 395))

def processPauseButton():
    global is_playing
    global play_index
    if is_playing:
        pg.mixer.pause()
        is_playing = False
        play_index -=1
        changePlay()
    else:
        is_playing = True
        pg.mixer.unpause()
        play_index += 1
        changePlay()       

def left():
    global sound_queue, music_index
    sound_queue[music_index].stop()
    if(music_index == 0):
        music_index = len(sound_queue)
    is_playing = True
    music_index -= 1
    chagneSoundsImage()
    play_index = 1
    changePlay()
    sound_queue[music_index].play()

def right():
    global sound_queue, music_index
    sound_queue[music_index].stop()
    if(music_index == len(sound_queue) - 1):
        music_index = -1
    is_playing = True
    music_index += 1
    play_index = 1
    changePlay()
    chagneSoundsImage()
    sound_queue[music_index].play()

chagneSoundsImage()
changePlay() 

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                if 370 <= pg.mouse.get_pos()[0] <= 415 and 390 <= pg.mouse.get_pos()[1] <= 450:
                    processPauseButton()
                if 395 <= pg.mouse.get_pos()[1] <= 425 and 240 <= pg.mouse.get_pos()[0] <= 276:
                    left()
                if 395 <= pg.mouse.get_pos()[1] <= 425 and 500 <= pg.mouse.get_pos()[0] <= 540:
                    right()
        elif event.type == pg.KEYDOWN:
            press = pg.key.get_pressed()
            if press[pg.K_SPACE]:
                processPauseButton() 
            elif press[pg.K_LEFT]:
                left()
            elif press[pg.K_RIGHT]:
                right()
    pg.display.flip()