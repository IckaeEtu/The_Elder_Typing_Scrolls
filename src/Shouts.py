class Shouts:

    def __init__(self, words: str, cooldown: int, power: int) -> None:
        self.words: str = words
        self.cooldown: int = cooldown
        self.power: int = power

    # Getters
    def get_words(self) -> str:
        return self.words

    def get_cooldown(self) -> int:
        return self.cooldown

    def get_power(self) -> int:
        return self.power

    # Setters
    def set_words(self, new_words: str) -> None:
        self.words = new_words

    def set_cooldown(self, new_cooldown: int) -> None:
        self.cooldown = new_cooldown

    def set_power(self, new_power: int) -> None:
        self.power = new_power


    def display_shout(self) -> None:
        print(f"Words: {self.words}, Cooldown: {self.cooldown}, Power: {self.power}")
