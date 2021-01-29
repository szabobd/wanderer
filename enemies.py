from cell import Cell
import random


class Enemy:
    def __init__(self, floors, area_level):
        floor_tile = floors[random.randint(1, len(floors) - 1)]
        self.x = floor_tile[0]
        self.y = floor_tile[1]
        percentage_number = random.randint(1, 10)
        self.level = None
        if percentage_number <= 5:
            self.level = area_level
        elif percentage_number <= 9:
            self.level = area_level + 1
        else:
            self.level = area_level + 2

        self.image = "skeleton"
        self.is_boss = False
        hp = 2 * self.level * random.randint(1, 6)
        self.hp = hp
        self.current_hp = hp
        self.dp = self.level / 2 * random.randint(1, 6)
        self.sp = self.level * random.randint(1, 6)
        self.is_alive = True
        self.has_key = False

    def draw(self, canvas, resource, image_size):
        canvas.create_image(self.x * image_size + (image_size / 2) + 2,
                            self.y * image_size + (image_size / 2) + 2, image=resource.get_image(self.image))

    def get_stats(self, canvas):
        canvas.create_text(350, 780, fill="black", font="Arial 14 bold",
                           text="Skeleton (Level 1) HP: " + str(self.current_hp) + "/" + str(self.hp) + " | DP: " + str(
                               self.dp) + " | SP: " + str(self.sp))


class Boss:
    def __init__(self, floors, area_level):
        floor_tile = floors[random.randint(1, len(floors) - 1)]
        self.x = floor_tile[0]
        self.y = floor_tile[1]
        percentage_number = random.randint(1, 10)
        self.level = None
        if percentage_number <= 5:
            self.level = area_level
        elif percentage_number <= 9:
            self.level = area_level + 1
        else:
            self.level = area_level + 2

        self.image = "boss"
        self.is_boss = True
        hp = 2 * self.level * random.randint(1, 6) + random.randint(1, 6)
        self.hp = hp
        self.current_hp = hp
        self.dp = self.level / 2 * random.randint(1, 6) + random.randint(1, 6) / 2
        self.sp = self.level * random.randint(1, 6) + random.randint(1, 6)
        self.is_alive = True
        self.has_key = False

    def draw(self, canvas, resource, image_size):
        canvas.create_image(self.x * image_size + (image_size / 2) + 2,
                            self.y * image_size + (image_size / 2) + 2, image=resource.get_image(self.image))

    def get_stats(self, canvas):
        canvas.create_text(350, 780, fill="black", font="Arial 14 bold",
                           text="Boss (Level 1) HP: " + str(self.current_hp) + "/" + str(self.hp) + " | DP: " + str(
                               self.dp) + " | SP: " + str(self.sp))


class Enemies:
    def __init__(self, area_level, grid):
        nr_of_enemies = random.randint(3, 6)
        self.enemy_list = []

        for i in range(nr_of_enemies):
            self.enemy_list.append(Enemy(grid.floors, area_level))

        enemy_with_key = random.randint(0, 2)
        self.enemy_list[enemy_with_key].has_key = True

        self.enemy_list.append(Boss(grid.floors, area_level))
