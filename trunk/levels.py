import game
import pygame
from wave_manager import Wave
import objairplane
from game import arena, get_resource
from random import randint
import objgun
from copy import copy

initialized = 0
file2wave = []

small_fighters_speed = 2.1
small_fighters_life = 21
small_fighters_shotspeed = 5
small_fighters_gun = objgun.LightGun()
inv_small_fighters_gun = objgun.InvLightGun()

war_airplanes_speed = 1.8
war_airplanes_life = 42
war_airplanes_shotspeed = 8
war_airplanes_leftgun = objgun.LeftRedBallGun()
war_airplanes_rightgun = objgun.RightRedBallGun()

corsair_speed = 3.5
corsair_life = 31.5
corsair_shotspeed = 10.5
corsair_gun = objgun.LightGun()

gunner_speed = 2
gunner_life = 25
gunner_shotspeed = 10 
gunner_gun = objgun.LightGun()

nogunfighter_speed = 2.4
nogunfighter_life = 14

striker_speed = 3.2
striker_life = 25
striker_shotspeed = 9
striker_gun = objgun.LightGun()

fighter_speed = 1.2
fighter_life = 38.5
fighter_shotspeed = 9
fighter_gun = objgun.ArchGun()

def init(name):
    #print 'Calling init'
    global file2wave
    initialized = 1
    f = None
    try:
        f = open(get_resource(name+'.txt'))
    except:
        print 'Could not open waves mapping file: %s.' % name
        raise SystemError
    else:
        for line in f:
            line = line.strip()
            if line:
                #print line
                if line[0] == '#': continue
                else:  file2wave.append(line)
 
def makewave0(): return None, None
                
def makewave1():
    global small_fighters_speed, small_fighters_gun, small_fighters_life
    global small_fighters_shotspeed, small_fighters_speed
    pos = []
    enemies = []
    base_pos = [150, arena.top - 350]
    for i in range(3):
        enemies.append(objairplane.EnemyAirplane(small_fighters_life, objairplane.bluestalker_images,
                                     speedy=small_fighters_speed , gun=copy(small_fighters_gun), 
                                     shotspeed=small_fighters_shotspeed, direction=[0, 1]))
        pos.append([base_pos[0] + 150 * i, base_pos[1]])
       
    return Wave(enemies), tuple(pos)


def makewave2():
    global small_fighters_speed, small_fighters_gun, small_fighters_life
    global small_fighters_shotspeed, small_fighters_speed
    pos = []
    enemies = []
    base_pos = [300, arena.top - 50]
    for i in range(4):
        enemies.append(objairplane.EnemyAirplane(small_fighters_life, objairplane.greenstalker_images,
                                     speedy=small_fighters_speed, gun=copy(small_fighters_gun), 
                                     shotspeed=small_fighters_shotspeed, direction=[0, 1]))
        pos.append([base_pos[0] - 30 * i, base_pos[1] - 30 * i])
       
    return Wave(enemies), tuple(pos)

def makewave15():
    global small_fighters_speed, small_fighters_gun, small_fighters_life
    global small_fighters_shotspeed, small_fighters_speed
    pos = []
    enemies = []
    base_pos = [500, arena.top - 1000]
    for i in range(4):
        enemies.append(objairplane.EnemyAirplane(small_fighters_life, objairplane.greenstalker_images,
                                     speedy=small_fighters_speed, gun=copy(small_fighters_gun), 
                                     shotspeed=small_fighters_shotspeed, direction=[0, 1]))
        pos.append([base_pos[0] + 30 * i, base_pos[1] - 30 * i])
       
    return Wave(enemies), tuple(pos)

def makewave3():
    global small_fighters_speed, small_fighters_gun, small_fighters_life
    global small_fighters_shotspeed, small_fighters_speed
    pos = []
    enemies = []
    base_pos = [100, arena.top - 50*7]
    for i in range(4):
        enemies.append(objairplane.EnemyAirplane(small_fighters_life, objairplane.lightgreenstalker_images, 
                                     speedy=small_fighters_speed, gun=copy(small_fighters_gun), 
                                     shotspeed=small_fighters_shotspeed, direction=[0, 1]))
        
        pos.append([base_pos[0] + 30 * i, base_pos[1] + 50 * i])
       
    return Wave(enemies), tuple(pos)

def makewave4():
    global small_fighters_speed, small_fighters_gun, small_fighters_life
    global small_fighters_shotspeed, small_fighters_speed
    waves = []
    pos = []
    enemies = []
    base_pos = [300, arena.top - 50*7]
    for i in range(4):
        enemies.append(objairplane.EnemyAirplane(small_fighters_life, objairplane.yellowstalker_images, 
                                     speedy=small_fighters_speed, gun=copy(small_fighters_gun), 
                                     shotspeed=small_fighters_shotspeed, direction=[0, 1]))
        pos.append([base_pos[0] + 30 * i, base_pos[1] + 50 * i])
       
    return Wave(enemies), tuple(pos)

def makewave5():
    global small_fighters_speed, small_fighters_gun, small_fighters_life
    global small_fighters_shotspeed, small_fighters_speed
    waves = []
    pos = []
    enemies = []
    base_pos = [500, arena.top - 50]
    for i in range(4):
        enemies.append(objairplane.EnemyAirplane(small_fighters_life, objairplane.graystalker_images,
                                     speedy=small_fighters_speed, gun=copy(small_fighters_gun), 
                                     shotspeed=small_fighters_shotspeed, direction=[0, 1]))
        pos.append([base_pos[0] + 30 * i, base_pos[1] - 50 * i])
       
    return Wave(enemies), tuple(pos)

def makewave6():
    global war_airplanes_speed, war_airplanes_life
    global war_airplanes_leftgun, war_airplanes_rightgun, war_airplanes_shotspeed
    
    guns = [war_airplanes_leftgun, war_airplanes_rightgun]
    pos = []
    enemies = []
    base_pos = [100, arena.top - 50*7]
    
    for i in range(2):
            enemies.append(objairplane.EnemyAirplane(war_airplanes_life, objairplane.war_airplaneimages, 
                                    speedy=war_airplanes_speed, gun=copy(guns[i]), 
                                    shotspeed=war_airplanes_shotspeed, direction=[0, 1], size='big'))
            pos.append([base_pos[0] + 400 * i, base_pos[1]])
       
    return Wave(enemies), tuple(pos)

def makewave7():
    global inv_small_fighters_gun, small_fighters_life 
    global small_fighters_shotspeed, small_fighters_speed
    
    pos = []
    enemies = []
    for i in range(3):
        enemies.append(objairplane.EnemyAirplane(small_fighters_life, objairplane.inv_bluestalker_images, 
                                     speedx=small_fighters_speed/1.0,
                                     speedy=small_fighters_speed, gun=copy(inv_small_fighters_gun), 
                                     shotspeed=small_fighters_shotspeed, direction=[0, -1]))
        pos.append([140*i+260, arena.bottom+60])
    
    return Wave(enemies), tuple(pos)

def makewave8():
    global inv_small_fighters_gun, small_fighters_life 
    global small_fighters_shotspeed, small_fighters_speed
    
    pos = []
    enemies = []
    for i in range(3):
        enemies.append(objairplane.EnemyAirplane(small_fighters_life, objairplane.inv_yellowstalker_images, 
                                                 speedx=small_fighters_speed/1.35,
                                     speedy=small_fighters_speed, gun=copy(inv_small_fighters_gun), 
                                     shotspeed=small_fighters_shotspeed, direction=[-1, -1]))
        pos.append([200*i, arena.bottom+60])
    
    return Wave(enemies), tuple(pos)

def makewave9():
    global inv_small_fighters_gun, small_fighters_life 
    global small_fighters_shotspeed, small_fighters_speed
    
    pos = []
    enemies = []
    for i in range(3):
        enemies.append(objairplane.EnemyAirplane(small_fighters_life, objairplane.inv_greenstalker_images, speedx=small_fighters_speed/1.4,
                                     speedy=small_fighters_speed, gun=copy(inv_small_fighters_gun), 
                                     shotspeed=small_fighters_shotspeed, direction=[-1, -1]))
        pos.append([200*i, arena.bottom+60])
    
    return Wave(enemies), tuple(pos)

def makewave10():
    global corsair_gun, corsair_life, corsair_shotspeed, corsair_speed
    pos = []
    enemies = []
    for i in range(2):
        enemies.append(objairplane.EnemyAirplane(corsair_life, objairplane.corsair_image, speedy=corsair_speed,
                                     gun=copy(corsair_gun), shotspeed=corsair_shotspeed,
                                     direction=[0, 1]))
        pos.append([300*i+180, arena.top - 80])
    
    return Wave(enemies), tuple(pos)

def makewave11():
    global gunner_gun, gunner_life, gunner_shotspeed, gunner_speed
    pos = []
    enemies = []
    base_pos = [185, -50]
    for i in range(2):
        enemies.append(objairplane.EnemyAirplane(gunner_life, objairplane.gunner_images, speedx=gunner_speed/1.3,
                                     speedy=gunner_speed, gun=copy(gunner_gun), 
                                     shotspeed=gunner_shotspeed, direction=[0.9, 1], shottick=15, size='big'))
        
        pos.append([base_pos[0] + 120*i , base_pos[1]])
        
    return Wave(enemies), tuple(pos)

def makewave12():
    global fighter_gun, fighter_life, fighter_shotspeed, fighter_speed
    pos = []
    enemies = []
    
    enemies.append(objairplane.EnemyAirplane(fighter_life, objairplane.fighter_image, speedy=fighter_speed,
                                 gun=copy(fighter_gun), shotspeed=fighter_shotspeed,
                                 direction=[0, 1]))
    pos.append([arena.width/2-45, -80])
    
    return Wave(enemies), tuple(pos)
    
def makewave13():
    global nogunfighter_life, nogunfighter_speed
    pos = []
    enemies = []
    base_pos = [arena.width-190, -100]
    
    for i in range(4):
        enemies.append(objairplane.EnemyAirplane(nogunfighter_life, objairplane.nogunfighter_images,
                                     speedx=nogunfighter_speed/1.35, speedy=nogunfighter_speed, 
                                     direction=[-0.8, 1]))
        
        pos.append([base_pos[0] + 45*i, base_pos[1]])

    return Wave(enemies), tuple(pos)

def makewave14():
    global nogunfighter_life, nogunfighter_speed
    pos = []
    enemies = []
    base_pos = [190, -100]
    
    for i in range(4):
        enemies.append(objairplane.EnemyAirplane(nogunfighter_life, objairplane.nogunfighter_images,
                                     speedx=nogunfighter_speed/1.35, speedy=nogunfighter_speed, 
                                     direction=[0.8, 1]))
        
        pos.append([base_pos[0] + 45*i, base_pos[1]])

    return Wave(enemies), tuple(pos)
        
def make():
    global file2wave
    if file2wave == []:
        return makewave0()
    wavetype = file2wave.pop(0)
    try:
        return globals()['makewave'+wavetype]()
    except Exception, e:
        print 'Exception in makewave function: ', str(e)
        #raise SystemError
    
def maxwavesperlevel():
    global file2wave
    j = 0
    for wave in file2wave:
        wave = wave.strip()
        if wave and wave <> '0': j+= 1
    return j
    
def maxlevels():
    return 2

def numrocks(level):
    if level >= maxlevels():
        return 18
    percent = float(level) / maxlevels()
    return int(percent * 12)

def maxsimwaves(level):
    if 0 <= level <= 5: return randint(1, 2)
    elif 6 < level <= 10: return randint(1, 3)
    elif 11 < level <= 15: return randint(2, 3)
    else: return 4

