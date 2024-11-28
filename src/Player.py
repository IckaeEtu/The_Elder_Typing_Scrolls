import Shouts


class PLayer:

    name: str
    health: float
    shouts: list
    level: int

    def __init__(self, name: str, health: float = 20.0, shouts: list = list(), level: int = 1) -> None:
        self.name = name 
        self.health = health
        self.shouts = shouts
        self.level = level

    # Getters
    def get_name(self) -> str:
        return self.name
    def get_health(self) -> float:
        return self.health
    def get_shouts(self) -> list:
        return self.shouts
    def get_level(self) -> int:
        return self.level
    
    #Setters
    def set_name(self, new_name: str) -> None:
        self.name = new_name
    def set_health(self, new_health: float) -> None:
        self.health = new_health
    def set_shouts(self, new_shouts: list) -> None:
        self.shouts = new_shouts
    def add_shout(self, shout: Shouts) -> bool:
        if shout not in self.shouts:
            self.shouts.append(shout)
            return True
        else:
            return False
    def remove_shout(self, shout: Shouts) -> bool:
        if shout in self.shouts:
            self.shouts.remove(shout)
            return True
        else:
            return False
    def set_level(self, new_level: int) -> None:
        self.level = new_level
    def levelup(self) -> None:
        self.level += 1;
    


