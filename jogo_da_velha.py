
import pygame #importa a biblioteca pygame para o script


# pygame configuração
pygame.init() #inicialização do pygame
pygame.font.init() #inicialização do pacote de fontes no pygame

screen = pygame.display.set_mode((600, 600)) #definição do tamanho da tela
pygame.display.set_caption('Jogo da Velha') #nome da janela do jogo
clock = pygame.time.Clock() #biblioteca de tempo

fonte_quadrinhos = pygame.font.SysFont('Comic Sans Ms', 100, True, True) #importar fonte
running = True #variável de controle do status do jogo

personagem_x = fonte_quadrinhos.render('X', True, 'red')
personagem_y = fonte_quadrinhos.render('O', True, 'red')
apresenta_personagem = 0
   
x=0
y=0
while running:
    # controle de enventos no jgo
    for event in pygame.event.get():
        # pygame.QUIT significa que quando usuário clicar em x a tela fechará
        if event.type == pygame.QUIT:
            running = False
        # pygame.MOUSEBUTTONDOWN significa evento de click do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('Clicou')
            click_pos = pygame.mouse.get_pos()
            print("eixo X=", click_pos[0])
            print("eixo Y=", click_pos[1])
            x=click_pos[0]
            y=click_pos[1]
            apresenta_personagem += 1
            if (apresenta_personagem>=9):
                 apresenta_personagem=0
                 screen.fill("black")
   
    #quadrantes
    #primeira linha
    Q1=0<x<200 and y<200 
    Q2=400>x>200 and y<200
    Q3=x>=400 and y<200
    #segunda linha
    Q4=x<200 and 400>y>=200
    Q5=400>=x>200 and 400>y>200
    Q6= x>400 and 400>y>200
    #terceira linha
    Q7=x<=200 and y>=400
    Q8=400>x>200 and y>=400
    Q9=x>=400 and y>=400

    if apresenta_personagem % 2:
     rodada=personagem_y
    else:
     rodada=personagem_x
    #Desenha tabuleiro
    #                                 origem      destino    
    #                                ( x , y)   ( x , y ) 
    pygame.draw.line(screen, 'white',(200, 0), (200, 600), 10)#linha vertical 1
    pygame.draw.line(screen, 'white',(400, 0), (400, 600), 10)#linha vertical 2
    pygame.draw.line(screen, 'white',(0, 200), (600, 200), 10)#linha horizontal 1
    pygame.draw.line(screen, 'white',(0, 400), (600, 400), 10)#linha horizontal 2

    #Primeira linha            x  y
    if Q1:
        screen.blit(rodada,(60,30)) #primeiro
    elif Q2:
        screen.blit(rodada,(260,30)) #segundo
    elif Q3:
        screen.blit(rodada,(460,30)) #terceiro
    #Segunda Linha               
    if Q4:
        screen.blit(rodada,(60,230)) #quarto
    elif Q5:
        screen.blit(rodada,(260,230)) #quinto
    elif Q6:
        screen.blit(rodada,(460,230)) #sexto
    #Terceira Linha               
    if Q7:
        screen.blit(rodada,(60,430)) #setimo
    elif Q8:
        screen.blit(rodada,(260,430)) #oitavo
    elif Q9:
        screen.blit(rodada,(460,430)) #nono

    # flip() o display para atualizar a página
    pygame.display.flip()

    clock.tick(60)  # limita o fps para 60

pygame.quit()