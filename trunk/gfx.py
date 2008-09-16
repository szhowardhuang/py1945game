"""graphics class, helps everyone to draw
Copyright Peter Shinners from SolarWolf.
"""

import sys, pygame, pygame.image
from pygame.locals import *

import game, map

#the accessible screen surface and size
surface = None
rect = Rect(0, 0, 0, 0)

#the accessable dirty rectangles
dirtyrects = []

tile_image = None

wantscreentoggle = 0


def initialize(size, fullscreen):
    global surface, rect, starobj, tile_image
    try:
        flags = 0
        if fullscreen:
            flags |= FULLSCREEN
        depth = pygame.display.mode_ok(size, flags, 16)
        surface = pygame.display.set_mode(size, flags, depth)
        rect = surface.get_rect()

        pygame.mouse.set_visible(0)

#        if surface.get_bytesize() == 1:
#            loadpalette()
        
        tile_image = load(game.get_resource('1945.bmp'))

    except pygame.error, msg:
        print 'Error msg: ', msg
        raise pygame.error, 'Cannot Initialize Graphics: %s' % str(msg)
        

def switchfullscreen():
    oldfull = surface.get_flags() & FULLSCREEN == FULLSCREEN
    newfull = game.display == 1
    if newfull == oldfull:
        return
    global wantscreentoggle
    wantscreentoggle = 1


def dirty(rect):
    dirtyrects.append(rect)


def dirty2(rect1, rect2):
    if not rect2:
        dirtyrects.append(rect1)
    elif rect.colliderect(rect2):
        dirtyrects.append(rect1.union(rect2))
    else:
        dirtyrects.append(rect1)
        dirtyrects.append(rect2)


def update():
    global dirtyrects
    pygame.display.update(dirtyrects)
    del dirtyrects[:]

#    global wantscreentoggle
#    if wantscreentoggle:
#        wantscreentoggle = 0
#        if game.handler:
#            starobj.eraseall(game.handler.background, sys.modules[__name__])
#        screencapture = pygame.Surface(surface.get_size())
#        screencapture.blit(surface, (0,0))
#        clipcapture = surface.get_clip()
#        initialize(surface.get_size(), game.display)
#        surface.blit(screencapture, (0,0))
#
#        pygame.display.update()
#        surface.set_clip(clipcapture)

def optimize(img):
    #~ if surface.get_alpha():
        #~ img.set_alpha()
        #~ if surface.get_flags() & HWSURFACE:
            #~ img.set_colorkey(0)
        #~ else:
            #~ img.set_colorkey(0, RLEACCEL)
    #~ elif not surface.get_flags() & HWSURFACE:
    if not surface.get_flags() & HWSURFACE:
        clear = img.get_colorkey()
        if clear:
            img.set_colorkey(clear, RLEACCEL)
    return img.convert()

def load(name, ckey=(0, 67, 171)):
    img = load_raw(name)
    
    img.set_alpha(None)
    img.set_colorkey(ckey)
    return img.convert()

def load_raw(name):
    #file = game.get_resource(name)
    #img = pygame.image.load(file)
    img = pygame.image.load(game.get_resource(name))
    return img

#===============================================================================
# 
# def animstrip(img, width=0, height=0, ckey=(0, 0, 0)):
#    if not width:
#        width = img.get_width()
#    if not height:
#        height = img.get_height()       
#    size = width, height   
#    images = []
# #    origalpha = img.get_alpha()
# #    origckey = img.get_colorkey()
# #    img.set_colorkey(None)
# #    img.set_alpha(None)
#    for x in range(0, img.get_width(), width):
#        i = pygame.Surface(size)
#        i.blit(img, (0, 0), ((x, 0), size))
# #        if origalpha:
# ##            print 'image has alpha channel'
# #            i.set_colorkey((0,0,0))
# #        elif origckey:
# ##            print 'image has origin colorkey'
# #            i.set_colorkey(origckey)
#        #i.set_colorkey(ckey)
#        #i.set_alpha(255)
#        #i.set_colorkey(None)
#        images.append(i)
# #    img.set_alpha(origalpha)
# #    img.set_colorkey(origckey)
#    return images
#===============================================================================

def animstrip(img, width=0, ckey=None):
    if not width:
        width = img.get_height()
    size = width, img.get_height()
    images = []
    
    origalpha = img.get_alpha()
    
    origckey = img.get_colorkey()
    
    img.set_colorkey(None)
    
    img.set_alpha(None)
    for x in range(0, img.get_width(), width):
        i = pygame.Surface(size)
        i.blit(img, (0, 0), ((x, 0), size))
        if origalpha:
            i.set_colorkey((0,0,0))
        elif origckey:
            i.set_colorkey(origckey)
        images.append(optimize(i))
    img.set_alpha(origalpha)
    img.set_colorkey(origckey)
    return images
    