import pygame, sys
from soldiers import Soldier
from info import *
from botao import Button
from tabuleiro import Tabuleiro
from menu import Menu


def jogo():
    pygame.init()
    fps = 60

    janela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('tabuleiro')

    ativo = True
    clock = pygame.time.Clock()
    tabuleiro = Tabuleiro(largura, altura, linhas, tam_quadrados)
    
    while ativo:
        clock.tick(fps)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ativo = False

        tabuleiro.grade_loop(janela)
        pygame.display.update()

    pygame.quit()   

def menu_principal():
    pygame.init()
    clock = pygame.time.Clock()
    janela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Menu Principal")
    menu_principal = Menu()
    tabuleiro = Tabuleiro(largura, altura, linhas, tam_quadrados)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                jogo()
                #pos = pygame.mouse.get_pos()
                c = event.pos[0] // (largura // 11)
                l = event.pos[1] // (altura // 11)
                tabuleiro.click(l, c)
                return
                
        janela.fill(preto)
        menu_principal.desenhar_menu(janela)
        pygame.display.flip()
        clock.tick(60)

menu_principal()

pygame.quit()
