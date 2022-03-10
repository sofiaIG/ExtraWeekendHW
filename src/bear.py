class Bear:
    def __init__(self, bear_name, stomach):
        self.bear_name = bear_name
        self.stomach = stomach

    def take_fish_from_river(self, river, fish):
        river.remove(fish)
        self.stomach.append(fish)

    def count_fish_in_stomach(self):
        return len(self.stomach)

    def sleep_bear(self):
        self.stomach.clear()
        return self.stomach


        


