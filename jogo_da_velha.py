#Importa a biblioteca pygame
import pygame

# Configuração pygame
pygame.init() #inicialização do pygame
pygame.display.set_caption("Jogo da Velha") #nome da janela
icon = pygame.image.load("icone.png")  #define qual é o logo 
pygame.font.init() #Inicializa o pacote de fontes do pygame
pygame.display.set_icon(icon)   #define o logo no janela ao lado do titulo 
screen = pygame.display.set_mode((1280, 720)) #define o tamanho da janela
clock = pygame.time.Clock() #biblioteca de tempo
running = True #variavel que indica que está "funcionado/aberto"
font = pygame.font.SysFont("Impact", 74)  # 'None' usa a fonte padrão, 74 é o tamanho da fonte
person_X = font.render("X",True,"red")
person_O = font.render("O",True,"blue")
click=0
while running:      #loop enquanto a variavel running for true 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #evento que registra o click no "X" da janela
            running = False           #quando for clicado define a variavel running como false e encerra o jogo
        if event.type==pygame.MOUSEBUTTONDOWN:
             click += 1
             if(click>2):
                click=1
    # Limpa a tela
    screen.fill("black")

    # Desenha X ou O com base no contador de cliques
    if click == 1:
        screen.blit(person_X, (500, 350))  # Desenha "X"
    elif click == 2:
        screen.blit(person_O, (500, 350))  # Desenha "O"

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()