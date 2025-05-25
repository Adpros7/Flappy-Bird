from pygame import *

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Flappy Bird")
background = pygame.transform.scale(pygame.image.load("flappySky.png").convert(), (500, 500))
window.blit(background, (0, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("space was pressed")
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
