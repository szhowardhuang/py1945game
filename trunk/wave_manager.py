"""
Modulo wave_manager
Gerencia os waves (grupo de inimigos)
"""
from objairplane import EnemyAirplane

class Wave:
    """
    Definicao do objeto wave
    """
    def __init__(self, enemies):
        """
        Parametros:
        enemies - lista de inimigos
        """
        self.enemies = enemies
        
    def tick(self, speedadjust=1.0):
        """
        Atualiza o wave
        """
        for enemy in self.enemies:
            if enemy.dead:
                self.enemies.remove(enemy)
            else: 
                enemy.tick(speedadjust)
    
    def start(self, enemies_pos):
        """
        Inicializa os inimigos nas posicoes
        dadas.
        Parametros:
        enemies_pos - lista de posicoes dos inimigos
        """
        i = 0
        for enemy in self.enemies:
            enemy.start(enemies_pos[i])
            i += 1
            
    def draw(self, gfx):
        [enemy.draw(gfx) for enemy in self.enemies]
            
    def erase(self, background):
        [enemy.erase(background) for enemy in self.enemies]
    
    def dead(self):
        for enemy in self.enemies:
            if not enemy.dead:
                return 0
        return 1
    
        
        
                                 