import pygame
from info import *

class Button:
    def __init__(self, txt, pos, largura, altura, cor, cor_mouse_cima):
        self.texto = txt
        self.pos = pos
        self.largura = largura
        self.altura = altura
        self.cor = cor
        self.cor_mouse_cima = cor_mouse_cima
        self.botao = pygame.Rect(self.pos, 
                                 (self.largura, self.altura))

    def desenhar(self, janela):
        if self.botao.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(janela, self.cor_mouse_cima, self.botao)
        else:
            pygame.draw.rect(janela, self.cor, self.botao)
            fonte = pygame.font.Font(None, 20)
            texto_renderizado = fonte.render(self.texto, 
                                            True, branco)
            retangulo_texto = texto_renderizado.get_rect(center=self.botao.center)
            janela.blit(texto_renderizado, retangulo_texto)

    def verificar_click(self):
        if self.botao.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False