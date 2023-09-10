
import pygame
import random
import sys
import time

class Quadrado:

    def __init__(self,cor,pos_x,pos_y,largura_objeto=50,altura_objeto=50,) -> None:
        self.cor = cor
        self.largura_objeto = largura_objeto
        self.altura_objeto = altura_objeto
        self.pos_x = pos_x
        self.pos_y = pos_y

        

class Game:

    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    N_RODADAS = 10
    
    rodada = 0
    cores = [RED,GREEN,BLUE]

    tempos_reacao =[]


    def __init__(self,largura=800,altura=600,name ="Jogo de Reação" ) -> None:

        self.largura  = largura
        self.altura = altura
        self.name = name
        #self.tela = pygame.display.set_mode((largura, altura))
        pygame.init()
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption(self.name)
        self.tela.fill(Game.WHITE)

        self.reaction_times =[]
        self.hits=0
        self.miss=0

    def gera_quadrado_random(self):

        x = random.randint(50, self.largura - 50)
        y = random.randint(50, self.altura - 50)
        cor = random.choice(Game.cores)

        return Quadrado(cor=cor,pos_x=x,pos_y=y)
    
    def vefifica_acerto(self,tecla):
        pass

    def end_game(self):
        fonte = pygame.font.SysFont('arial',10,True)
        mensagem = f"Acertos: {self.hits}\nErro:{self.miss}\nTempo médio de reação : {len(self.reaction_times)/sum(self.reaction_times)}"

        msg_formatado = fonte.render(mensagem,True,(0,0,0))
        self.tela.blit(msg_formatado,(400,300))
    
    def start_round(self):

        self.tela.fill(Game.WHITE)
        pygame.display.update()

        Game.rodada += 1
        pygame.time.delay(random.randint(1000, 3000))
        quadrado = self.gera_quadrado_random()
        pygame.draw.rect(self.tela, 
                         quadrado.cor,
                        (quadrado.pos_x, quadrado.pos_y, quadrado.largura_objeto,quadrado.altura_objeto)
                        )
        
        pygame.display.update()

        start_time = time.time()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    end_time = time.time()
                    self.reaction_time = end_time - start_time

                    if quadrado.cor == Game.RED:
                        if event.key == pygame.K_r:
                            self.hits += 1
                        else:
                            self.miss +=1     
                        self.reaction_times.append(self.reaction_time)
                        return
                    
                    if quadrado.cor == Game.GREEN:
                        if event.key == pygame.K_g:
                            self.hits += 1
                        else:
                            self.miss +=1     
                        self.reaction_times.append(self.reaction_time)
                        return
                    
                    if quadrado.cor == Game.BLUE:
                        if event.key == pygame.K_b:
                            self.hits += 1
                        else:
                            self.miss +=1     
                        self.reaction_times.append(self.reaction_time)
                        return
                   



    
    def run(self):
        

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if Game.rodada < Game.N_RODADAS:
                    self.start_round()
                    print(f"acertos: {self.hits}  erros: {self.miss}\nTempo Reacao:{self.reaction_time }")

                self.tela.fill(Game.WHITE)
                self.end_game()
                pygame.display.update()



jogo = Game()
jogo.run()
    




