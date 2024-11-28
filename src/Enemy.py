import Shouts


class Ennemy:
    name: str
    health: float
    strength: float
    weakness: list

    def __init__(self, name: str, health: float = 20.0, strength: float = 2.5, weakness: list = list()) -> None:
        self.name = name
        self.health = health
        self.strength = strength
        self.weakness = weakness

    #Getters
    def get_name(self) -> str:
        return self.name
    def get_health(self) -> str:
        return self.health
    def get_strenght(self) -> float:
        return self.strength
    def get_weakness(self) -> list:
        return self.weakness


    #Setters
    def add_weakness(self,shout: Shouts):
        if shout not in self.weakness:
            self.weakness.append(shout)
    def remove_weakness(self,shout: Shouts):
        if shout in self.weakness:
            self.weakness.remove(shout)

    def take_damage(self,damage: float):
        self.health -= damage
    
    