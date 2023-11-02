import pygame
from sprites import *
from config import *
import sys


class Game:
    def __init__(self):
        pygame.init()  # initialize pygame to be used
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # Game Window
        self.clock = pygame.time.Clock()  # Sets frame rate
        self.running = True

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)

    def new(self):  # a new game starts
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()  # contained all characters, walls, enemy
        self.blocks = pygame.sprite.LayeredUpdates()  # walls
        self.enemies = pygame.sprite.LayeredUpdates()  # enemy
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

    def events(self):  # Game loop event
        for event in pygame.event.get():  # get every event that happens in pygame
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):  # Game loop updates
        self.all_sprites.update()  # find the update method in every sprite and will run the method, sprites.py

    def draw(self):  # Game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)  # draws the sprites on the window
        self.clock.tick(FPS)  # Set Frame Rate
        pygame.display.update()

    def main(self):  # Game loop
        while self.playing:
            self.events()  # Key Press
            self.update()  # Update game so its not a static image
            self.draw()  # Display all sprites to out screen
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass


g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
