
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
    YELLOW = (255,255,0)

    N_RODADAS = 10
    
    rodada = 0
    cores = [RED,GREEN,BLUE,YELLOW]

    tempos_reacao =[]


    def __init__(self,largura=1024,altura=768,name ="Jogo de Reação" ) -> None:

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

    def tela_end_game(self):
        fonte = pygame.font.SysFont('arial',18,True)

        mensagem1 = f"Acertos: {self.hits} Erro:{self.miss} Tempo médio de reação : {len(self.reaction_times)/sum(self.reaction_times)}"
        msg_formatado = fonte.render(mensagem1,True,(0,0,0))
        self.tela.blit(msg_formatado,((self.largura//2) - 150, 150))

        y_offset = 15
        
        for i, reaction_time in enumerate(self.reaction_times):
            texto_tempo = fonte.render(f"Rodada {i + 1}: {reaction_time:.2f} ms", True, (0, 0, 0))
            self.tela.blit(texto_tempo, (self.largura // 2 - 150, self.altura // 4 + y_offset))
            y_offset += 15
    
    def tela_inicial(self):
        
        contagem = 3
        while contagem != -1:
            self.tela.fill(Game.WHITE)
            pygame.display.update()
            msg = f'Incia em {contagem}'
            fonte = pygame.font.SysFont('arial',25,True)
            msg_formatado = fonte.render(msg,True,(0,0,0))
            self.tela.blit(msg_formatado,((self.largura//2) - 200, self.altura//2))
            pygame.display.update()
            pygame.time.delay(2000)

            contagem-=1



    
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
                        if event.key == pygame.K_RIGHT:
                            self.hits += 1
                        else:
                            self.miss +=1     
                        self.reaction_times.append(self.reaction_time)
                        return
                    
                    if quadrado.cor == Game.GREEN:
                        if event.key == pygame.K_UP:
                            self.hits += 1
                        else:
                            self.miss +=1     
                        self.reaction_times.append(self.reaction_time)
                        return
                    
                    if quadrado.cor == Game.BLUE:
                        if event.key == pygame.K_LEFT:
                            self.hits += 1
                        else:
                            self.miss +=1     
                        self.reaction_times.append(self.reaction_time)
                        return
                    
                    if quadrado.cor == Game.YELLOW:
                        if event.key == pygame.K_DOWN:
                            self.hits += 1
                        else:
                            self.miss +=1     
                        self.reaction_times.append(self.reaction_time)
                        return                   
                if event.type == pygame.QUIT:
                    return

                   



    
    def run(self):
        
        self.tela_inicial()
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if Game.rodada < Game.N_RODADAS:
                    self.start_round()
                    print(f"acertos: {self.hits}  erros: {self.miss}\nTempo Reacao:{self.reaction_time }")
                else:
                    self.tela.fill(Game.WHITE)
                    self.tela_end_game()
                    pygame.display.update()



jogo = Game()
jogo.run()
    




