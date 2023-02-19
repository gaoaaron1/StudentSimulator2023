import pygame
from config import *
import math
import random 

class Spritesheet:
    def __init__(self, file):
        #load sprite sheet
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        #cut from sprite sheet    
        sprite = pygame.Surface([width, height])
        #select cut outs from loaded image
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        #cuts out black background
        sprite.set_colorkey(BLACK)
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        #player direction
        self.facing = 'down'

        self.animation_loop = 1


        #create a sprite sheet
        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)


        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        #animation positions
        self.down_animations = [self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 2, self.width, self.height)]

        self.up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

        self.left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

        self.right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]


    def update(self):
        #render and updates the user's movements
        self.movement()

        #animate our user
        self.animate()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0

    #Player movement method
    def movement(self):
        keys = pygame.key.get_pressed()

        #press left arrow key
        if keys[pygame.K_LEFT]:

            #move all sprites to have camera follow player
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED

            self.x_change -= PLAYER_SPEED
            self.facing = 'left'

        #press right arrow key
        if keys[pygame.K_RIGHT]:

            #move all sprites to have camera follow player
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED


            self.x_change += PLAYER_SPEED
            self.facing = 'right'    

        #press up arrow key
        if keys[pygame.K_UP]:

            #move all sprites to have camera follow player
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED


            self.y_change -= PLAYER_SPEED
            self.facing = 'up'

        #press down arrow key
        if keys[pygame.K_DOWN]:

            #move all sprites to have camera follow player
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED

            self.y_change += PLAYER_SPEED
            self.facing = 'down'    

    #detect collisions        
    def collide_blocks(self, direction):  
        
        #horizontal collisions
        if direction == "x":

            #we assign hit to the game block
            #False - check whether we want to delete sprite when collide
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                #moving right
                if self.x_change > 0:
                    #first align with block then 
                    #since we subtract self.rect.width, we go beside block
                    self.rect.x = hits[0].rect.left - self.rect.width
                    
                    #cancels out the camera movement
                    for sprite in self.game.all_sprites:
                        sprite.rect.x += PLAYER_SPEED

                #moving left    
                if self.x_change < 0:  
                    self.rect.x = hits[0].rect.right      

                    #cancels out the camera movement
                    for sprite in self.game.all_sprites:
                        sprite.rect.x -= PLAYER_SPEED
                        

        #vertical collisions
        if direction == "y":
            #we assign hit to the game block
            #False - check whether we want to delete sprite when collide
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                #moving down
                if self.y_change > 0:
                    #first align with block then 
                    #since we subtract self.rect.height, we take away height
                    self.rect.y = hits[0].rect.top - self.rect.height
                
                    #cancels out the camera movement
                    for sprite in self.game.all_sprites:
                        sprite.rect.y += PLAYER_SPEED
                        

                #moving up    
                if self.y_change < 0:  
                    self.rect.y = hits[0].rect.bottom    

                    #cancels out the camera movement
                    for sprite in self.game.all_sprites:
                        sprite.rect.y -= PLAYER_SPEED
                        

    def animate(self):

        if self.facing == "down":
            #if stand still, set image to static image
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                #otherwise we move, and use animations
                self.image = self.down_animations[math.floor(self.animation_loop)]
                #every 10 frames change animation
                self.animation_loop += 0.1

                #when after iterating 3 images set animation to 1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
            
        if self.facing == "up":
            #if stand still, set image to static image
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height)
            else:
                #otherwise we move, and use animations
                self.image = self.up_animations[math.floor(self.animation_loop)]
                #every 10 frames change animation
                self.animation_loop += 0.1

                #when after iterating 3 images set animation to 1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
            
        if self.facing == "left":
            #if stand still, set image to static image
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height)
            else:
                #otherwise we move, and use animations
                self.image = self.left_animations[math.floor(self.animation_loop)]
                #every 10 frames change animation
                self.animation_loop += 0.1

                #when after iterating 3 images set animation to 1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
            
        if self.facing == "right":
            #if stand still, set image to static image
            if self.x_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height)
            else:
                #otherwise we move, and use animations
                self.image = self.right_animations[math.floor(self.animation_loop)]
                #every 10 frames change animation
                self.animation_loop += 0.1

                #when after iterating 3 images set animation to 1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

#instance for walls
class EmptyBlock(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

#instance for walls
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

#create instance of ground
class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(64, 352, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

#menu button
class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('junegull.ttf', fontsize)
        self.content = content
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg
        
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    #collides with mouse and pressed
    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False


