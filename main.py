import pygame

pygame.init()

screen = pygame.display.set_mode((1344, 720))
clock = pygame.time.Clock()

# PLAYER
player_img = pygame.image.load('player_light_blue.png')
mano_bomba = pygame.image.load('gfx/mano_bomba.png')

# CENARIO
piso = pygame.image.load('gfx/TileFree.png')
parede = pygame.image.load('gfx/TileWall.png')

# BOMBA
bomba_image = pygame.image.load('gfx/bomb.png')

VELOCIDADE = 1
TAMANHO = 48

class Cenario:

    def __init__(self, jogador):
        self.mano_bomba = jogador
        self.tamanho = 48
        self.matriz = [
            
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2],
                [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2],
                [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2],
                [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
                [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
                [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2],
                [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],

        ]
    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            if coluna == 3:
                cor = (0, 255, 255)
                pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
                tela.blit(bomba_image, (x+14, y+14, self.tamanho, self.tamanho))
            if coluna == 2:
                cor = (50, 50, 50)
                # tela.blit(parede, (x, y, self.tamanho, self.tamanho))
                pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                cor = (0, 255, 255)
                # tela.blit(piso, (x, y, self.tamanho, self.tamanho))
                pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
    def pintar(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)
    
    def calcular_regras(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    self.matriz[self.mano_bomba.linha][self.mano_bomba.coluna] = 3
        col = self.mano_bomba.coluna_intencao
        lin = self.mano_bomba.linha_intencao
        if 0 <= col <= 27 and 0 <= lin <= 14:
            if self.matriz[lin][col] != 2:
                self.mano_bomba.aceitar_movimento()
        

class Bomba:
    def __init__(self, jogador):
        self.jogador = jogador
        self.coluna = 1
        self.linha = 1
        self.bomb = bomba_image
    
    def plantar_bomba(self):
        print('plantou a bomba')

def planta_bomba():
    screen.blit(bomba_image, (58, 58))

class Player:

    def __init__(self):
        self.coluna = 1
        self.linha = 1
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha
        self.vel_x = 0
        self.vel_y = 0
        self.x = 100
        self.y = 100
        self.player_surf = mano_bomba
        self.player_rect = self.player_surf.get_rect(topleft=(self.coluna*TAMANHO, self.linha*TAMANHO))

    def mostra_player(self, tela):
        tela.blit(self.player_surf, self.player_rect)
        
    
    def calcular_regras(self):
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        self.player_rect.left = self.coluna * TAMANHO
        self.player_rect.top = self.linha * TAMANHO

    def processar_eventos(self, eventos, tela):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    self.vel_x = VELOCIDADE
                elif evento.key == pygame.K_LEFT:
                    self.vel_x = -VELOCIDADE  

                elif evento.key == pygame.K_UP:
                    self.vel_y = -VELOCIDADE
                elif evento.key == pygame.K_DOWN:
                    self.vel_y = VELOCIDADE 

                        
            elif evento.type == pygame.KEYUP:

                if evento.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif evento.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif evento.key == pygame.K_UP:
                        self.vel_y = 0
                elif evento.key == pygame.K_DOWN:
                    self.vel_y = 0


    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

player = Player()
bomba = Bomba(player)
cenario = Cenario(player)


while True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    
        
        
    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    cenario.pintar(screen)
    pygame.time.delay(100)
    player.mostra_player(screen)
    
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    eventos = pygame.event.get()
    player.calcular_regras()
    cenario.calcular_regras(eventos)
    player.processar_eventos(eventos, screen)