import os
import pymclevel
from models import MCWorld, MCMap

def get_worlds():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    saves_dir = os.path.join(current_dir, "..", "..", "saves")
    worlds = []
    for name in os.listdir(saves_dir):
        world_dir = os.path.join(saves_dir, name)
        if os.path.isdir(world_dir) and name != "CraftMap" and os.path.isfile(os.path.join(world_dir, "level.dat")):
            icon_path = os.path.join(world_dir, "icon.png")
            world = MCWorld(name, icon_path)
            worlds.append(world)
    return worlds
