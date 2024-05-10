import pygame, sys

titulo = "Tabuleiro"
largura, altura = 600, 600
linhas, colunas = 11, 11
tam_quadrados = largura//linhas

#cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
cinza = (128, 128, 128)

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

class Menu:
    def __init__(self):
        self.botao_iniciar = Button("Iniciar", 
                                    (largura // 2 - 50, altura // 2 - 25), 100, 50, azul, cinza)

    def desenhar_menu(self, janela):
        janela.fill(preto)
        self.botao_iniciar.desenhar(janela)

    def verificar_botao(self):
        return self.botao_iniciar.verificar_click()

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = []
        self.lado_1 = self.lado_2 = 12 #quantas peças temos?

    def quadrados(self, janela):
        #base preta
        janela.fill(preto)
        for l in range(linhas):
            for c in range(l % 2, linhas, 2):
                cor = cinza if (l + c) % 2 == 0 else branco
                pygame.draw.rect(
                    janela, 
                    cor, 
                    (l*tam_quadrados, c*tam_quadrados, tam_quadrados, tam_quadrados))


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
                return


        tabuleiro.quadrados(janela)
        pygame.display.update()

    pygame.quit()   

def menu_principal():
    pygame.init()
    janela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Menu Principal")
    menu_principal = Menu()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                jogo()
                return
                
        janela.fill(preto)
        menu_principal.desenhar_menu(janela)
        pygame.display.update()

pygame.quit()

menu_principal()

