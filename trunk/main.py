"""main module, starts game and main loop"""

import pygame
import game, gfx, snd, txt
import allmodules
import gamepref
import gameplay
from pygame.locals import *


#at this point, all needed pygame modules should
#be imported, so they can be initialized at the
#start of main()

def main(args):
    try:
        gamemain(args)
        
    except KeyboardInterrupt:
        print 'Keyboard Interrupt...'
        print 'Exiting'


def gamemain(args):
    #initialize all our code (not load resources)
    pygame.init()
    game.clock = pygame.time.Clock()

    gamepref.load_prefs()

    full = 1
    gfx.initialize(game.size, full)
    pygame.display.set_caption('Py1945')

    #input.init()
    snd.initialize()
    if not txt.initialize():
        raise pygame.error, "Pygame Font Module Unable to Initialize"

    #create the starting game handler
    from gameinit import GameInit
    from gamefinish import GameFinish
    game.handler = GameInit(GameFinish(None))

    gamestart = pygame.time.get_ticks()
    numframes = 0

    #main game loop
    lasthandler = None
    while game.handler:
        numframes += 1
        handler = game.handler
        if handler != lasthandler:
            lasthandler = handler
            if hasattr(handler, 'starting'):
                handler.starting()
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                fps = game.clock.get_fps()
                continue
            elif event.type == pygame.ACTIVEEVENT:
                if event.state == 4 and event.gain:
                    #uniconified, lets try to kick the screen
                    pygame.display.update()
                elif event.state == 2:
                    if hasattr(game.handler, 'gotfocus'):
                        if event.gain:
                            game.handler.gotfocus()
                        else:
                            game.handler.lostfocus()
                continue
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN and event.mod&pygame.KMOD_ALT:
                    game.display = not game.display
                    gfx.switchfullscreen()
                    continue
                else:
                    handler.input(event)
            elif event.type == pygame.QUIT:
                game.handler = None
                break
            handler.event(event)
        handler.run()
        game.clockticks = game.clock.tick(40)
        gfx.update()
        
        while not pygame.display.get_active():
            pygame.time.wait(100)
            pygame.event.pump()

    gameend = pygame.time.get_ticks()

    runtime = (gameend - gamestart) / 1000.0


    #game is finished at this point, do any
    #uninitialization needed
    gamepref.save_prefs()
    pygame.quit()


if __name__ == '__main__':
    import sys
    main(sys.argv)
