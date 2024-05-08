class Soldier:
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def is_valid_move(self, board, new_x, new_y):
         #verifica se os movimentos são válidos dentro dos limites do tabuleiro
         if 0 <= new_x < board.width and 0 <= new_y < board.height:
             return board.grid[new_y][new_x] == 0
         return False
    
    def get_neighbors(self, board):
        #retorna os vizinhos válidos no tabuleiro
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_x = self.x + dx
                new_y = self.y + dy
                if self.is_valid_move(board, new_x, new_y):
                    neighbors.append((new_x, new_y))
        return neighbors
    
    def calculate_movement_cost(self, board, new_x, new_y):
        #calcula o custo do movimento para o soldado
        if board.grid[new_y][new_x] == 0:
            return 1
        else:
            return 1.5
        
    def move_to(self, board, new_x, new_y):
        #move o soldado para a posição especificada
        if self.is_valid_move(board, new_x, new_y):
            self.move(new_x, new_y)
            return True
        return False
