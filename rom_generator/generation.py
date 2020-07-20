import argparse
import copy
import random
import generator as gen
import scriptFunctions as scripts

def makeKey(project, x, y):
    a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")
    return makeKey(a_rock_sprite, x, y)

def makeLock(project, x, y):
    a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")
    return makeLock(a_rock_sprite, x, y)

def makeScene(project, scene):
    scene.append(makeKey(project, rand(), rand()))
    scene.append(makeLock(project, rand(), rand()))
    return scene