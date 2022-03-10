class River:
    def __init__(self, fish_stock):
        self.fish_stock = fish_stock

    def add_fish_to_river(self, fish):
        self.fish_stock.append(fish)
        return self.fish_stock