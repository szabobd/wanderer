from tkinter import *
from resource import Resource
from grid import Grid
from hero import Hero
from enemies import *
from area import Area
import random

image_size = 72
board_size = 10
root = Tk()
canvas = Canvas(root, width=image_size * board_size, height=image_size * board_size + 100)
grid = Grid(board_size)
hero = Hero()
area = Area(grid)
background = Resource()
level = 1


def on_key_press(e):
    if not hero.is_alive:
        canvas.create_rectangle(0, 720, 720, 820, fill='white')
        canvas.create_text(350, 770, fill="black", font="Arial 14 bold",
                           text="GAME OVER, YOU ARE DEAD, WASTED")
        return
    is_tile_occupied = hero.is_tile_occupied(area.enemy_list)
    if e.keycode == 65:
        hero.erase(canvas, background, image_size)
        if grid.grid[hero.x - 1][hero.y].cell_type == "floor" and hero.x - 1 >= 0 and not is_tile_occupied:
            hero.x = hero.x - 1
        hero.image = "hero_left"
        hero.draw(canvas, background, image_size)
    elif e.keycode == 68:
        hero.erase(canvas, background, image_size)
        if hero.x + 1 <= 9 and grid.grid[hero.x + 1][hero.y].cell_type == "floor" and not is_tile_occupied:
            hero.x = hero.x + 1
        hero.image = "hero_right"
        hero.draw(canvas, background, image_size)
    elif e.keycode == 83:
        hero.erase(canvas, background, image_size)
        if hero.y + 1 <= 9 and grid.grid[hero.x][hero.y + 1].cell_type == "floor" and not is_tile_occupied:
            hero.y = hero.y + 1
        hero.image = "hero_down"
        hero.draw(canvas, background, image_size)
    elif e.keycode == 87:
        hero.erase(canvas, background, image_size)
        if grid.grid[hero.x][hero.y - 1].cell_type == "floor" and hero.y - 1 >= 0 and not is_tile_occupied:
            hero.y = hero.y - 1
        hero.image = "hero_up"
        hero.draw(canvas, background, image_size)
    elif e.keycode == 32:
        if is_tile_occupied:
            current_enemy = hero.get_enemy_on_same_tile(area.enemy_list)
            hero.strike(current_enemy, canvas, background, image_size, area)
            if hero.killed_boss and hero.has_key:
                area.level += 1
                area.draw(grid, hero, canvas, background, image_size)
    canvas.create_rectangle(0, 720, 720, 820, fill='white')
    if hero.is_tile_occupied(area.enemy_list):
        current_enemy = hero.get_enemy_on_same_tile(area.enemy_list)
        current_enemy.get_stats(canvas)

    if not hero.is_alive:
        canvas.create_rectangle(0, 720, 720, 820, fill='white')
        canvas.create_text(350, 770, fill="black", font="Arial 14 bold",
                           text="GAME OVER, YOU ARE DEAD, WASTED")
    else:
        hero.get_stats(canvas)


canvas.bind("<KeyPress>", on_key_press)
canvas.pack()
canvas.focus_set()
canvas.delete("all")

area.draw(grid, hero, canvas, background, image_size)


root.mainloop()
