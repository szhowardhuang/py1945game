#hud class

import pygame
from pygame.locals import *
import game, gfx, txt

labelfont = None
valuefont = None

def load_game_resources():
    #print 'Load game resources from hud'
    global labelfont, valuefont
    fontname = 'stencil'
    valuefont = (txt.Font(fontname, 15), (255, 255, 255))
    labelfont = (txt.Font(fontname, 15), (221, 92, 14))

class HUD:
    
    def __init__(self):
        self.drawsurface = gfx.surface
        
        self.lastscore = 0
        self.lastlevel = 0
        self.lastgun = None
        self.lastlive = 0
        self.lastwave = 0
        
        self.labelgunarea = Rect(game.arena.left + 100, game.arena.bottom + 20, 60, 20)
        self.valuegunarea = Rect(game.arena.left + 170, game.arena.bottom + 20, 80, 20)
        self.labelscorearea  = Rect(game.arena.left + 95, game.arena.bottom + 45, 60, 20)
        self.valuescorearea  = Rect(game.arena.left + 165, game.arena.bottom + 45, 70, 20)
        
        self.labellivesarea  = Rect(game.arena.left + 390, game.arena.bottom + 20, 40, 20)
        self.valuelivesarea  = Rect(game.arena.left + 440, game.arena.bottom + 20, 50, 20)
        
        self.labelwavesarea  = Rect(game.arena.left + 263, game.arena.bottom + 40, 100, 30)
        self.valuewavesarea  = Rect(game.arena.left + 365, game.arena.bottom + 40, 60, 30)
               
        #self.labellevelarea  = Rect(game.arena.left + 150, game.arena.bottom + 20, 120, 30)
        #self.valuelevelarea  = Rect(game.arena.left + 150, game.arena.bottom + 20, 120, 30)
        
        #self.area = Rect(game.arena.left, game.arena.bottom, game.arena.width, game.size[1] - game.arena.height)

    def drawlives(self, lives, fast=0):
        if lives < 0: lives = 0
        
        #Draw life label
        text = 'Life: '
        f, c = labelfont
        t = f.text(c, text, self.labellivesarea.topleft)
        self.drawsurface.blit(t[0], t[1])
        gfx.dirty(self.labellivesarea)
        
        #Draw life value
        text = ' %02d ' % lives
        f, c = valuefont
        t = f.text(c, text, self.valuelivesarea.topleft)
        self.livescleanup()
        self.drawsurface.blit(t[0], t[1])
        gfx.dirty(self.valuelivesarea)

    def drawscore(self, score, fast=0):
        #print 'Draw score'
        
        #Draw score label
        text = 'Score: '
        f, c = labelfont
        t = f.text(c, text, self.labelscorearea.topleft)
        self.drawsurface.blit(t[0], t[1])
        gfx.dirty(self.labelscorearea)
        
        #Draw score value
        text = ' %06d ' % score
        f, c = valuefont
        t = f.text(c, text, self.valuescorearea.topleft)
        self.scorecleanup()
        self.drawsurface.blit(t[0], t[1])
        gfx.dirty(self.valuescorearea)

    
    def drawgun(self, playergun): 
        
        #Draw gun label
        text = 'Gun: '
        f, c = labelfont
        t = f.text(c, text, self.labelgunarea.topleft)
        self.drawsurface.blit(t[0], t[1])
        gfx.dirty(self.labelgunarea)
        
        #Draw gun value
        self.lastgun = playergun
        text = ' %20s ' % playergun
        f, c = valuefont
        t = f.text(c, text, self.valuegunarea.topleft)
        self.guncleanup()
        self.drawsurface.blit(t[0], t[1])
        gfx.dirty(self.valuegunarea)
    
    def drawwaves(self, wave):
        
        #Draw wave label
        text = 'Waves Left: '
        f, c = labelfont
        t = f.text(c, text, self.labelwavesarea.topleft)
        self.drawsurface.blit(t[0], t[1])
        gfx.dirty(self.labelwavesarea)
        
        #Draw wave value
        self.lastwave = wave
        text = ' %02d ' % self.lastwave
        f, c = valuefont
        t = f.text(c, text, self.valuewavesarea.topleft)
        self.wavescleanup()
        self.drawsurface.blit(t[0], t[1])
        gfx.dirty(self.valuewavesarea)
    
    def scorecleanup(self):
        gfx.surface.fill((0, 0, 0), self.valuescorearea)
       
    def wavescleanup(self):
         gfx.surface.fill((0, 0, 0), self.valuewavesarea)
         
    def guncleanup(self):
        gfx.surface.fill((0, 0, 0), self.valuegunarea)

    def livescleanup(self):
        gfx.surface.fill((0, 0, 0), self.valuelivesarea)
                
    def drawlevel(self, level, fast=0):
        dest = self.drawsurface
        offset = self.drawoffset
        if not fast:
            r = self.poslevel
            r2 = dest.blit(self.imghud1, r, r).move(offset)
        else:
            r2 = None
        if self.lastlevel != level:
            self.lastlevel = level
            self.imglevel = score.render(level)
            self.poslevel = self.imglevel.get_rect()
            self.poslevel.center = 50, 565
        r1 = dest.blit(self.imglevel, self.poslevel).move(offset)
        gfx.dirty2(r1, r2)
    
    def draw(self, player, wave):
        self.drawscore(player.score)
        if player.nextgun: self.drawgun(player.nextgun.name)
        elif player.gun: self.drawgun(player.gun.name)
        self.drawlives(player.lives)
        self.drawwaves(wave)
        
        

        
