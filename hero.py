from cell import Cell
import random


class Hero:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.level = 1
        self.has_key = False
        self.image = "hero_down"
        self.del_image = "floor"
        self.cell = Cell(self.x, self.y, "hero_down")
        hp = 20 + (3 * random.randint(1, 6))
        self.max_hp = hp
        self.current_hp = hp
        self.dp = 2 * random.randint(1, 6)
        self.sp = 5 + random.randint(1, 6)
        self.killed_boss = False
        self.is_alive = True

    def draw(self, canvas, resource, image_size):
        canvas.create_image(self.x * image_size + (image_size / 2) + 2,
                            self.y * image_size + (image_size / 2) + 2, image=resource.get_image(self.image))

    def next_level_area_reset(self):
        self.x = 0
        self.y = 0
        self.has_key = False
        self.killed_boss = False

    def erase(self, canvas, resource, image_size):
        canvas.create_image(self.x * image_size + (image_size / 2) + 2,
                            self.y * image_size + (image_size / 2) + 2, image=resource.get_image(self.del_image))

    def is_tile_occupied(self, monsters):
        for monster in monsters:
            if monster.x == self.x and monster.y == self.y and monster.is_alive:
                return True
        return False

    def strike(self, enemy, canvas, resource, image_size, area):
        hero_sv = 2 * random.randint(1, 6) + self.sp
        enemy_sv = 2 * random.randint(1, 6) + enemy.sp

        if hero_sv > enemy.dp:
            enemy.hp = enemy.hp + enemy.dp - hero_sv

            if enemy.hp <= 0:
                if enemy.has_key:
                    self.has_key = True
                if enemy.is_boss:
                    self.killed_boss = True
                enemy.is_alive = False
                self.erase(canvas, resource, image_size)
                self.draw(canvas, resource, image_size)
                self.level_up()

        if enemy_sv > self.dp:
            self.current_hp = self.current_hp + self.dp - enemy_sv

            if self.current_hp <= 0:
                self.is_alive = False

    def get_enemy_on_same_tile(self, enemies):
        for enemy in enemies:
            if enemy.x == self.x and enemy.y == self.y:
                return enemy

    def get_stats(self, canvas):
        canvas.create_text(350, 750, fill="black", font="Arial 14 bold",
                           text="Hero (Level " + str(self.level) + ") HP: " + str(self.current_hp) + "/" + str(
                               self.max_hp) + " | DP: " + str(
                               self.dp) + " | SP: " + str(self.sp))

    def level_up(self):
        self.level += 1
        self.max_hp += random.randint(1, 6)
        self.dp += random.randint(1, 6)
        self.sp += random.randint(1, 6)
