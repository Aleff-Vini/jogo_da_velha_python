# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
pygame.display.set_caption("Jogo da Velha")
icon = pygame.image.load("icone.png")  
pygame.display.set_icon(icon)  
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
cor_sel=0
cores =["blue","red","green","yellow","white","brown"]
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cor_sel += 1
            print(cor_sel)
    if cor_sel==len(cores):
     cor_sel=0
 
    screen.fill(cores[cor_sel])

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()