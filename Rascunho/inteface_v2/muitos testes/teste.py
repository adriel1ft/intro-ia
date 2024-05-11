import pygame
import sys

titulo = "Tabuleiro"
largura, altura = 600, 600
linhas, colunas = 11, 11
tam_quadrados = largura // linhas

# cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
cinza = (128, 128, 128)

class MainMenu:
    def __init__(self):
        self.botao_x = largura // 2 - 50
        self.botao_y = altura // 2 - 25
        self.botao_largura = 100
        self.botao_altura = 50
        self.botao_cor = azul
        self.botao_cor_hover = (0, 100, 255)

    def desenhar_menu(self, janela):
        janela.fill(preto)
        fonte = pygame.font.Font(None, 36)
        texto = fonte.render("Iniciar Jogo", True, branco)
        texto_retangulo = texto.get_rect(center=(largura // 2, altura // 2))
        janela.blit(texto, texto_retangulo)
        pygame.draw.rect(janela, self.botao_cor, (self.botao_x, self.botao_y, self.botao_largura, self.botao_altura))

    def verificar_botao(self, pos_mouse):
        if self.botao_x <= pos_mouse[0] <= self.botao_x + self.botao_largura:
            if self.botao_y <= pos_mouse[1] <= self.botao_y + self.botao_altura:
                return True
        return False

def jogo():
    pygame.init()
    fps = 60

    janela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('tabuleiro')

    ativo = True
    clock = pygame.time.Clock()
    tabuleiro = Tabuleiro()

    while ativo:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ativo = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu.verificar_botao(pygame.mouse.get_pos()):
                    return

        tabuleiro.quadrados(janela)
        pygame.display.update()

    pygame.quit()

def main_menu():
    pygame.init()
    janela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Menu Principal")
    global main_menu
    main_menu = MainMenu()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if main_menu.verificar_botao(pygame.mouse.get_pos()):
                    return

        janela.fill(preto)
        main_menu.desenhar_menu(janela)
        pygame.display.update()

main_menu()
jogo()
