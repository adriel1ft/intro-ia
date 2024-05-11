import pygame
from info import *
from soldiers import Soldier
from botao import Button

class Menu:
    def __init__(self):
        self.botao_iniciar = Button("Iniciar", 
                                    (largura // 2 - 50, altura // 2 - 25), 100, 50, azul, cinza)

    def desenhar_menu(self, janela):
        janela.fill(preto)
        self.botao_iniciar.desenhar(janela)

    def verificar_botao(self):
        return self.botao_iniciar.verificar_click()
