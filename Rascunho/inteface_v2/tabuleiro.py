import pygame, sys
from info import *

class Tabuleiro:
    def __init__(self, largura, altura, linhas, tam_quadrados):
        self.largura = largura
        self.altura = altura
        self.linhas = linhas
        self.tam_quadrados = tam_quadrados
        self.grade = [[0] * 11 for _ in range(11)] 
        self.peca_selecionada = None
        self.comeca = 1  #jogadores
        self.inicializa_pecas()

    def inicializa_pecas(self):
        self.grade[0][5] = -1 #azul
        self.grade[10][5] = 1 #vermelho  

    def quadrados(self, janela):
        largura = self.largura
        altura = self.altura
        tam_quadrados = self.tam_quadrados
        
        #base preta
        janela.fill(preto)
        for l in range(self.linhas):
            for c in range(self.linhas):
                cor = cinza if (l + c) % 2 == 0 else branco
                pygame.draw.rect(
                    janela, 
                    cor, 
                    (l*tam_quadrados, c*tam_quadrados, tam_quadrados, tam_quadrados))

        #desenha peças
        for l in range(11):
            for c in range(11):
                if self.grade[l][c] != 0:
                    cor_peca = vermelho if self.grade[l][c] == 1 else azul
                    pygame.draw.circle(
                        janela, 
                        cor_peca, 
                        (c * tam_quadrados + tam_quadrados // 2, l * tam_quadrados + tam_quadrados // 2),
                        tam_quadrados // 3)

        # Desenha a peça selecionada
        if self.peca_selecionada:
            l, c = self.peca_selecionada
            pygame.draw.rect(janela, vermelho, (c * tam_quadrados, l * tam_quadrados, tam_quadrados, tam_quadrados), 3)
    
    def click(self, l, c):
        if self.peca_selecionada:
            if self.valida_movimento(l, c):
                self.grade[l][c] = self.comeca
                self.grade[self.peca_selecionada[0]][self.peca_selecionada[1]] = 0
                self.peca_selecionada = None
                self.comeca *= -1  #muda para o próximo jogador
        else:
            if self.grade[l][c] == self.comeca:
                self.peca_selecionada = (l, c)

    def valida_movimento(self, l, c):
        dx = abs(l - self.peca_selecionada[0])
        dy = abs(c - self.peca_selecionada[1])
        return (dx <= 1 and dy <= 1) and self.grade[l][c] == 0


    def grade_loop(self, janela):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                c = pos[0] // (self.largura // 11)
                l = pos[1] // (self.altura // 11)
                for soldier in self.soldiers:
                    if 0 <= l < 11 and 0 <= c < 11:
                        #move o soldado para a posição do mouse
                        self.click(l, c)
        
        self.quadrados(janela)
        pygame.display.update()
