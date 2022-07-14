import pygame

pygame.init() #Inicia o pygame "Biblioteca python para games"
x = 300 #Controlar a posição do jogador em X
y = 300 #Controlar a posição do jogador em Y
pos_x = 240 #Controlar a posição do npc em X
pos_y = 700 #Controlar a posição do npc em Y
velocidade = 20 #A velocidade do jogador
velo_npc = 20 # A velocidade do npc
fundo = pygame.image.load('fundo.png') #Define a imagem de fundo do game
carro = pygame.image.load('Sem título.png') #Define o jogador
npc_1 = pygame.image.load('carro1.png') #Define o 1º npc
npc_2 = pygame.image.load('carro2.png') #Define o 2º npc

janela = pygame.display.set_mode((600,600)) #Variavel janela "Interface " recebe o tamanho que deverá ser
pygame.display.set_caption("Jogo criado em pytho") #Titulo no cabeçalho da interface

janela_aberta = True #Outra variavel para controle de fechar e abrir a janela


while janela_aberta: #Loop de repetição para que a janela permaneça aberta enquanto não é clicado para sair
    pygame.time.delay(50)
    for event in pygame.event.get(): #Loop para os eventos do game
        if event.type == pygame.QUIT: #Se fechar a janela do game
            janela_aberta = False #Janela desaparece
    comandos = pygame.key.get_pressed() #Controle dos botoes do teclado
    if comandos[pygame.K_UP]: #Se clicado para cima
        y -= velocidade
    if comandos[pygame.K_DOWN]:#Se clicado para baixo
        y += velocidade
    if comandos[pygame.K_RIGHT]:#Se clicado para esquerda
        x += velocidade
    if comandos[pygame.K_LEFT]:#Se clicado para direita
        x -= velocidade

    if (pos_y <= -200): #Se o npc chegar ao topo então ele reaparece no comeco da interface
        pos_y = 600 #Posicao que o npc reaparece
    pos_y -= velo_npc #A velocidade do npc

    #Detecção de colisão
    if((x + 20 > pos_x and y + 100 > pos_y)):
        y = 1200
    if((x - 20 < pos_x and y + 100 > pos_y)):
        y = 1200
    #if ((x + 20 > pos_x and y + 100 > pos_y)) and if((x - 20 < pos_x and y + 100 > pos_y)):
        #y = 1200

    #Fazendo as imagens aparecer na janela
    janela.blit(fundo,(0,30))
    janela.blit(carro,(x,y))
    janela.blit(npc_1,(pos_x,pos_y))
    janela.blit(npc_2,(pos_x + 250,pos_y))

    #Para atualizar a posicao do jogado, npc e afins
    pygame.display.update()
pygame.quit()#Fim do programa