import pygame
import sys
import math
from info import *

# Definições de cores
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
CINZA = (128, 128, 128)
BRANCO = (255, 255, 255)

# Configurações do jogo
TAM_QUADRADOS = tam_quadrados

# Classe para representar o tabuleiro do jogo
class Board:
    def __init__(self):
        self.grid = [[0] * 8 for _ in range(8)]
        self.selected_piece = None
        self.turn = 1  # 1 para jogador 1 (vermelho), -1 para jogador 2 (azul)
        self.initialize_pieces()

    def initialize_pieces(self):
        # Posições iniciais dos jogadores
        self.grid[1][0] = -1  # Jogador 2 (azul)
        self.grid[6][7] = 1   # Jogador 1 (vermelho)

    def draw(self, screen):
        for row in range(8):
            for col in range(8):
                color = BRANCO if (row + col) % 2 == 0 else CINZA
                pygame.draw.rect(screen, color, (col * TAM_QUADRADOS, row * TAM_QUADRADOS, TAM_QUADRADOS, TAM_QUADRADOS))
                if self.grid[row][col] != 0:
                    piece_color = VERMELHO if self.grid[row][col] == 1 else AZUL
                    pygame.draw.circle(screen, piece_color,
                                       (col * TAM_QUADRADOS + TAM_QUADRADOS // 2, row * TAM_QUADRADOS + TAM_QUADRADOS // 2),
                                       TAM_QUADRADOS // 3)

        if self.selected_piece:
            row, col = self.selected_piece
            pygame.draw.rect(screen, VERMELHO, (col * TAM_QUADRADOS, row * TAM_QUADRADOS, TAM_QUADRADOS, TAM_QUADRADOS), 3)

    def handle_click(self, row, col):
        if self.selected_piece:
            if self.is_valid_move(row, col):
                self.grid[row][col] = self.turn
                self.grid[self.selected_piece[0]][self.selected_piece[1]] = 0
                self.selected_piece = None
                self.turn *= -1  # Muda para o próximo jogador
        else:
            if self.grid[row][col] == self.turn:
                self.selected_piece = (row, col)

    def is_valid_move(self, row, col):
        dx = abs(row - self.selected_piece[0])
        dy = abs(col - self.selected_piece[1])
        return (dx <= 1 and dy <= 1) and self.grid[row][col] == 0

# Função principal do jogo
def main():
    pygame.init()
    screen = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Damas")
    clock = pygame.time.Clock()
    board = Board()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // TAM_QUADRADOS
                row = event.pos[1] // TAM_QUADRADOS
                if 0 <= row < 8 and 0 <= col < 8:
                    board.handle_click(row, col)

        screen.fill(preto)
        board.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
