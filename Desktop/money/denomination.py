
class Self:
    def __init__(self, notes, coins):
        self.notes = notes
        self.coins = coins

    def display(self):
        print(f"Notes: {self.notes}")
        print(f"Coins: {self.coins}")

# Example usage:
me = Self(notes=5, coins=20)
me.display()
