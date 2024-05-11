import pygame as pg

TITLE = "Tabuleiro"
TILES_HORIZONTAL = 11
TILES_VERTICAL = 11
TILE_SIZE = 50
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Soldier:
    def __init__(self, surface, team, x, y):
        self.surface = surface
        self.team = team
        self.pos = (x, y)

    def draw(self):
        color = RED if self.team == "vermelho" else BLUE
        pg.draw.circle(self.surface, color, self.pos, TILE_SIZE // 2)

    def move(self, target):
        x = (TILE_SIZE * (target[0] // TILE_SIZE)) + TILE_SIZE // 2
        y = (TILE_SIZE * (target[1] // TILE_SIZE)) + TILE_SIZE // 2

        self.pos = (x, y)


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        pg.display.set_caption(TITLE)
        self.surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.loop = True
        self.soldiers = [
            Soldier(self.surface, "vermelho", 4 * TILE_SIZE, 0),
            Soldier(self.surface, "azul", 4 * TILE_SIZE, 10 * TILE_SIZE)
        ]

    def main(self):
        while self.loop:
            self.grid_loop()
        pg.quit()

    def grid_loop(self):
        self.surface.fill((0, 0, 0))
        for row in range(TILES_HORIZONTAL):
            for col in range(row % 2, TILES_HORIZONTAL, 2):
                pg.draw.rect(
                    self.surface,
                    (40, 40, 40),
                    (row * TILE_SIZE, col * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                )
        for soldier in self.soldiers:
            soldier.draw()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.loop = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.loop = False
            elif event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                for soldier in self.soldiers:
                    soldier.move(pos)

        pg.display.update()


if __name__ == "__main__":
    mygame = Game()
    mygame.main()
