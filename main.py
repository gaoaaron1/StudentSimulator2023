import pygame
from sprites import *
from config import *
from hud import *

import sys

class Game:
    def __init__(self):
        pygame.init()

        #create window
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('junegull.ttf', 32)
        self.running = True
        
        #score
        self.score_font = pygame.font.Font('junegull.ttf', 24)
        self.score = 0

        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.intro_background = pygame.image.load('./img/introbackground.png')

        # center the title text
        title_text = 'Student Simulator'
        title = self.font.render(title_text, True, BLACK)
        title_rect = title.get_rect()
        title_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT // 3)

        # center the button
        button_width, button_height = 100, 50
        button_x = (WIN_WIDTH - button_width) // 2
        button_y = WIN_HEIGHT // 2
        play_button = Button(button_x, button_y, button_width, button_height, WHITE, BLACK, 'Play', 32)


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

                #For every "BB" or black block create an black layer wall
                if column == "X":
                    #Create black wall object
                    EmptyBlock(self, j, i)    

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

        #initialize seconds
        timerSeconds = 2400;

        #create a timer object
        self.timer = Timer(self, timerSeconds * 1000)

        #create term label object
        #self.terms = Term(Game)

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

        #score label
        score_label = self.score_font.render(f'Score: {self.score}', True, WHITE)
        score_rect = score_label.get_rect(topright=(WIN_WIDTH - 10, 10))
        self.screen.blit(score_label, score_rect)

        # game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.timer.update()
        self.timer.draw()
        #self.terms.draw()
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
        self.timer.update()
        self.timer.draw()
        game_over_text = self.font.render('Game Over', True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(WIN_WIDTH//2, WIN_HEIGHT//2))
        self.screen.blit(game_over_text, game_over_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        

    #title screen for render
    def intro_screen(self):
        intro = True

        title = self.font.render('Student Simulator', True, BLACK)
        title_rect = title.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2.5))

        button_width = 100
        button_height = 50
        button_x = (WIN_WIDTH - button_width) // 2
        button_y = (WIN_HEIGHT - button_height) // 2
        play_button = Button(button_x, button_y, button_width, button_height, WHITE, BLACK, 'Play', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()    

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    timer = Timer(Game, 30)
    #terms = Terms(Game)
    g.game_over()

pygame.quit()
sys.exit()



