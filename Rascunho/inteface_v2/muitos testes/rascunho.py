def conquista_territorio(self, x, y, team):
        self.grid[y][x] = team  # Atualiza o tabuleiro para refletir a conquista do território

        # Determina a linha de surgimento dos novos soldados com base no time
        if team == 1:
            new_soldier_y = 0  # Linha superior do tabuleiro
        else:
            new_soldier_y = self.rows - 1  # Linha inferior do tabuleiro

        # Determina a coluna do quadrado do meio
        new_soldier_x = self.cols // 2

        # Adiciona um novo soldado na posição do quadrado do meio na linha de surgimento
        self.add_soldier(new_soldier_x, new_soldier_y, team)

        # Adiciona um novo soldado na posição do quadrado do meio na linha de surgimento contrária
        self.add_soldier(new_soldier_x, self.rows - new_soldier_y - 1, 3 - team)

