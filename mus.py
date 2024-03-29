import pygame as pg
import os

pg.init()

screen = pg.display.set_mode((800, 600))
BACKGROUND = pg.image.load('assets\\bckg.png').convert()
BACKGROUND = pg.transform.scale(BACKGROUND, (800, 600))
screen.blit(BACKGROUND, (0, 0))
is_playing = True

sound_files = os.listdir('music\\')
sound_images = os.listdir('assets\\sound_image\\')
sound_images.sort()
sound_files.sort()
sound_queue = []
for filename in sound_files:
    sound = pg.mixer.Sound('music\\' + filename)
    sound_queue.append(sound)
music_index = 0
sound_queue[music_index].play()

def chagneSoundsImage():
    SOUND_IMAGE = pg.image.load('assets\\sound_image\\' + sound_images[music_index]).convert()
    SOUND_IMAGE = pg.transform.scale(SOUND_IMAGE, (300, 315))
    screen.blit(SOUND_IMAGE, (240, 36))
chagneSoundsImage()
 

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif pg.mouse.get_pressed()[0]:
            if 370 <= pg.mouse.get_pos()[0] <= 430 and 382 <= pg.mouse.get_pos()[1] <= 452:
                if is_playing:
                    pg.mixer.pause()
                    is_playing = False
                else:
                    is_playing = True
                    pg.mixer.unpause()

            if 395 <= pg.mouse.get_pos()[1] <= 425 and 240 <= pg.mouse.get_pos()[0] <= 276:
                sound_queue[music_index].stop()
                if(music_index == 0):
                    music_index = len(sound_queue)
                is_playing = True
                music_index -= 1
                chagneSoundsImage()
                sound_queue[music_index].play()

            if 395 <= pg.mouse.get_pos()[1] <= 425 and 500 <= pg.mouse.get_pos()[0] <= 540:
                sound_queue[music_index].stop()
                if(music_index == len(sound_queue) - 1):
                    music_index = -1
                is_playing = True
                music_index += 1
                chagneSoundsImage()
                sound_queue[music_index].play()
    pg.display.flip()

print(pg.mouse.get_pos())