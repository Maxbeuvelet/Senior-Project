import pygame
from sprites import *
from config import *
import sys
import random


class Game:
    def __init__(self):
        pygame.init()  # initialize pygame to be used
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  # Game Window
        self.clock = pygame.time.Clock()  # Sets frame rate
        self.running = True
        self.font = pygame.font.Font('arial.ttf', 32)

        self.character_spritesheet = SpriteSheet('img/character.png')  # Importing the character sprite
        self.terrain_spritesheet = SpriteSheet('img/terrain.png')
        self.enemy_spritesheet = SpriteSheet('img/enemy.png')
        self.attack_spritesheet = SpriteSheet('img/attack.png')
        self.intro_background = pygame.image.load('./img/introbackground.png')
        self.go_background = pygame.image.load('./img/gameover.png')
        self.score = 0
        self.speed_buffs = pygame.sprite.LayeredUpdates()

        self.player_speed_buff = 0
    def createTilemap(self):
        for i, row in enumerate(tilemap):  # i will be the position and row is the value
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "b":
                    Block(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)
                if column == "R":
                    Road(self, j, i)
                if column == "W":
                    Water(self, j, i)
                if column == "S":
                    SpeedBuff(self, j, i)

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y)
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y)

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

    def game_over(self):
        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))

        restart_button = Button(10, WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Restart', 32)

        for sprite in self.all_sprites:
            sprite.kill()
        print(self.score)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()
            self.screen.blit(self.go_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def intro_screen(self):
        intro = True
        title = self.font.render('499 Final', True, BLACK)
        title_rect = title.get_rect(x=10, y=10)
        play_button = Button(10, 50, 100, 50, WHITE, BLACK, 'Play', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos,mouse_pressed):
                intro = False
            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()


g = Game()  # Convert class into an object
g.intro_screen()  # Once the file is ran its going to run intro_screen
g.new()  # Set self.playing to True
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
