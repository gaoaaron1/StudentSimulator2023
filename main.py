import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()

        #create window
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        #self.font = pygame.font.Font('Arial', 32)
        self.running = True

        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')

    #Create our tile map 
    def createTileMap(self):    
        #enumerate will scan through elements of the array
        for i, row in enumerate(tilemap):
            #Gets content of column iterating through row
            for j, column in enumerate(row):

                #Create object for ground that covers entire terrain
                Ground(self, j, i)

                #For every B on tile create wall
                if column == "B":
                    #Creates wall object
                    Block(self, j, i)

                #For every P on tile create player
                if column == "P":
                    #Creates player object
                    Player(self, j, i)    

    def new(self):

        #A new game starts
        self.playing = True

        #Contains all sprites in game
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        #create tile map
        self.createTileMap()

    def events(self):
        #game loop events
        for event in pygame.event.get():
            #click close button closes app
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        # game loop updates
        self.all_sprites.update()

    def draw(self):
        # game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS) #update 60 fps
        pygame.display.update() #update screen

    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
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



