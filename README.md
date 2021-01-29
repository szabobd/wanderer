# Wanderer app home assignment for IBS and Greenfox examination

## Parts of the project:
The project contains seven .py files (area, hero, enemies, cell, grid, gamelogic and resource) and a directory for the eight gif files used in the project (4 hero, 2 enemy, 2 tile)
- **Resource:** This file handles the gifs used in the project, loading them when called by other classes
- **Cell:** This file creates the cells with the necessary attributes, which are the building blocks of the game area
- **Grid:** This file orders the cells into a playable area with walls and floor areas, based on the attributes given (like how big the game area should be)
- **Hero:** This file handles most of what the hero is capable of. These include: the stats of the hero, the position of the hero, the strike function of the hero and the level of the hero
- **Enemies:** This file handles the monsters of the game (skeletons and the boss). It draws them, assigns their number and stats, and provides the key which is needed to level up to a random monster
- **Area:** This file handles the monsters on different level of the game
- **Gamelogic:** This file makes makes the game work, meaning it uses other files and classes and executes them. It also handles the movement of the hero, including the change of image based on which way the hero is headed and the fact that he is not able to go to tiles which are walls


## Launching the game
1. Install Pythton 3.x to your system (the game was witten using 3.9)
2. Clone the repository to your PC
3. Open the directory that you pulled
4. Double click gamelogic.py

## Gameplay
When the game is running, the hero starts in the upper left corner of the maze. The hero needs to kill the boss and the skleton with the key to move on to the next level. The heros stats can be seen in the bottom, on a white rectangle. When in a battle with an enemy (hero on the same tile as the enemy), the stats of the enemy can be seen on this part as well. As long as the enemy standing on the same tile as the hero is alive, the hero can't move to other tiles. When the hero's life is less than 1, the HUD will say he is dead, and he cannot move. When the hero kill the boss and the skeleton with the key, he levels up, his stats go up and enters a new level with stronger enemies.

## Controls
- To move around, use `WASD`: move up = `W`, move down = `S`, move right = `D`, move left = `A`
- When on the same cell with an enemy, use `space` to attack

## Notes
There are some errors in the game:
- when the system renders two enemies on the same tile, and the hero enters that tile, they cannot be killed, as their HP will go below zero but the hero won't be able to move
- when the hero levels up, he will not gain any actual health, only his hp capacity grows
