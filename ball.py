import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill('white')
done = False
red = (255, 0, 0)
x = 400 
y = 300
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        press = pygame.key.get_pressed()
        if y>24:
            if press[pygame.K_UP]: y-=1
        if y<576:
            if press[pygame.K_DOWN]: y+=1
        if x>24:
            if press[pygame.K_LEFT]: x-=1
        if x<776:
            if press[pygame.K_RIGHT]: x+=1
        screen.fill('white')
        pygame.draw.circle(screen, red, (x, y), 24)
        pygame.display.flip()