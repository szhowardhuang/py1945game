#map class
import pygame
from pygame.locals import *
import gfx
from math import fabs
from random import randint, seed
from game import arena, get_resource

images = []
blue_background = pygame.surface.Surface((arena.width, arena.height))
seed(0)

def random_pos():
    y =  randint(65, 195)
    #print 'y = ', str(y)
    return y

def load_game_resources():
    global images, blue_background
    #print 'load game resources from map'
    blue_background.fill((0, 67, 171))
    
    images.append(gfx.load('island.png', ckey=None))
    images.append(gfx.load('terrain.png', ckey=None))
    images.append(gfx.load('volcano.png', ckey=None))
    
class Tile:
    def __init__(self, image, x, y):
        #print 'Creating tile...'
        self.image = image
        self.dead = 0
        self.imagerect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.lastrect = None
        
    def erase(self, background):
        gfx.dirty(self.lastrect)
        
    def tick(self):
        self.lastrect = Rect(self.rect)        
        x, y = self.rect.center
        y += 1
        self.rect.center = (x, y)     
        if self.rect.bottom > arena.bottom: 
            bottom1 = self.rect.bottom
            bottom2 = arena.bottom
            diff = bottom1 - bottom2
            self.rect.height -= fabs(diff)
            if self.rect.height <= 0:
              self.dead = 1
        #gfx.dirty2(self.rect, self.lastrect)
        
            
        
class TiledMap:
    """
    Simple tiled map
    """
    def __init__(self, name):
        self.rect = Rect(arena.top, arena.left, arena.width, arena.height)
        self.lastrect = None
        self.dead = False
        self.tiles = []
        self.tilesrect = []
        self.load(name)
        
    def load(self, name):
        try:
            f = open(get_resource(name+'.txt'))
        except:
            print 'Could not load map %s.' % name
            raise SystemError
        else:
            for line in f:
                if line[0] == '#': continue
                elif line.strip():
                    tname, tx, ty = line.split(';')
                    img = gfx.load(tname+'.png')
                    tx = int(tx)
                    ty = int(ty) 
                    if tx >= arena.width: tx = arena.width 
                    self.tiles.append(Tile(img, tx, ty))
            f.close()
            
    def draw(self):
        #blue_background.fill((0, 67, 171))
        for tile in self.tiles:
            if tile.dead:
                self.tiles.remove(tile)
            else:
                blue_background.fill((0, 67, 171), tile.lastrect)
                blue_background.blit(tile.image, tile.rect)
                
        gfx.surface.blit(blue_background, self.rect)
        gfx.dirty2(self.rect, self.lastrect)
        self.lastrect = Rect(self.rect)
                               
    def erase(self, background):
            
        if self.lastrect:
            background(self.lastrect)
            gfx.dirty(self.lastrect)
        else:
            background(self.rect)
            gfx.dirty(self.rect)
            
    def tick(self):
        """
        Ticking the map will tick all active tiles.
        """
        [tile.tick() for tile in self.tiles]
        
    def cleanup(self):            
        blue_background.fill((0, 67, 171))
        gfx.surface.blit(blue_background, self.rect)
        gfx.dirty2(self.rect, self.lastrect)
        self.lastrect = Rect(self.rect)
        
            
            
            
        

            
            