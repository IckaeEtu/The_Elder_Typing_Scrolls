import Enemy
import Player
import Shouts


class Game:
    player: Player
    enemies: list

    def __init__(self) -> None:
        self.player = Player("Dovahkiin", 100, 10)
        self.enemies = list()
    
    def start_game(self) -> None:
        print("Game started!")
        self.spawn_ennemy(Enemy("Draugr", 50, 10))

    def end_game(self) -> None:
        print("Game over!")

    def spaw_enemmy(self,enemy: Enemy = None) -> None:
        if enemy is not None:
            self.enemies.append(Enemy)
        print(f"Enemy {enemy.get_name()} has spawned, destroy it !")
    
    def select_enemy(self) -> Enemy:
        for id, enemy in enumerate(self.enemies):
            print(f"{id}: {enemy.get_name()} (Health: {enemy.get_health()}, Stregth: {enemy.get_strength()})")
        choice = int(input("Select the number of the one you want to slay"))
        return self.enemies[choice]
    
    def player_attack(self, shout: Shouts, enemy: Enemy) -> None:
        if shout.get_cooldown() > 0:
            print(f"{shout.get_words()} is on cooldown for {shout.get_cooldown()}")
        
        if shout in enemy.get_weakness():
            damage = shout.get_power() * 1.5
        else:
            damage = shout.get_power()
        
        enemy.take_damage(damage)
        shout.set_cooldown(3)
        print(f"{self.player.get_name()} used {shout.get_words()} on {enemy.get_name()} 
              dealing {damage} damage")
        
    def enemy_attack(self) -> None:
        if self.enemies:
            enemy = self.enemies[0]
            self.player.take_damage(enemy.get_strength())
            print(f"{self.player.get_name()} takes {enemy.get_strength} damages")

