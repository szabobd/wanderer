from tkinter import *


class Resource:

    def __init__(self):
        self.images = {}
        self.images["hero_up"] = self.load_image("gifs/hero-up.gif")
        self.images["hero_down"] = self.load_image("gifs/hero-down.gif")
        self.images["hero_right"] = self.load_image("gifs/hero-right.gif")
        self.images["hero_left"] = self.load_image("gifs/hero-left.gif")
        self.images["floor"] = self.load_image("gifs/floor.gif")
        self.images["wall"] = self.load_image("gifs/wall.gif")
        self.images["skeleton"] = self.load_image("gifs/skeleton.gif")
        self.images["boss"] = self.load_image("gifs/boss.gif")

    def load_image(self, path):
        img = PhotoImage(file=path)
        return img

    def get_image(self, key):
        return self.images[key]

