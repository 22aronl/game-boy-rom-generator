import argparse
import copy
import random
from generator import makeBasicProject, addSpriteSheet, makeBackground, makeScene, makeActor, addSymmetricSceneConnections, makeMusic, reverse_direction, initializeGenerator, writeProjectToDisk


def vijayaGame():
    
    # Set up a barebones project
    project = makeBasicProject()

    # Create sprite sheet for the player sprite
    player_sprite_sheet = addSpriteSheet(
        project, "player.png", "player", "player")
    project.settings["playerSpriteSheetId"] = player_sprite_sheet["id"]

    # add sprites
    a_rock_sprite = addSpriteSheet(project, "rock.png", "rock", "static")
    doorway_sprite = addSpriteSheet(project, "tower.png", "tower", "static")
    duck_sprite = addSpriteSheet(project, "duck.png", "duck", "animated", "2")
    
    # Add a background image
    default_bkg = makeBackground("placeholder.png", "placeholder")
    project.backgrounds.append(default_bkg)
    
    num_of_scenes = randInt(0, 30)
    for y in range(num_of_scenes)
        a_scene = copy.deepcopy(makeScene(f"Scene", default_bkg))
        for x in range(9)
            a_scene["actors"].append(actor2)


    """
    a_scene = copy.deepcopy(makeScene(f"Scene", default_bkg))
    a_scene2 = copy.deepcopy(makeScene(f"Scene", default_bkg))
    project.scenes.append(a_scene)
    project.scenes.append(a_scene2)
    """

    # Adding connections
    scene_connections_translations = {"right":0, "left":1, "up":2, "down":3}
    scene_connections = [[True, True, True, True] for n in range(2)]
    for y in range(2):
        for attempts in range(3):
            other_scene = random.randint(0, 2 - 2)
            if other_scene >= y:
                other_scene += 1
            chosen_direction = random.choice(["right", "left", "up", "down"])
            if scene_connections[y][scene_connections_translations[chosen_direction]]:
                if scene_connections[other_scene][scene_connections_translations[reverse_direction[chosen_direction]]]:
                    scene_connections[y][scene_connections_translations[chosen_direction]] = False
                    scene_connections[other_scene][scene_connections_translations[reverse_direction[chosen_direction]]] = False
                    addSymmetricSceneConnections(project, project.scenes[y], project.scenes[other_scene], chosen_direction, doorway_sprite)
                    break
                    

    # Get information about the background
    bkg_x = default_bkg["imageWidth"]
    bkg_y = default_bkg["imageHeight"]
    bkg_width = default_bkg["width"]
    bkg_height = default_bkg["height"]

    # Adding actors
    actor = makeActor(a_rock_sprite, 9, 8)
    actor2 = makeActor(a_rock_sprite, 2, 3)
    actor3 = makeActor(duck_sprite, 9, 10, "animated")
    a_scene['actors'].append(actor)
    a_scene['actors'].append(actor2)
    a_scene2['actors'].append(actor3)

    # add a sprite to indicate the location of a doorway
    # a better way to do this in the actual levels is to alter the background image instead
    doorway_sprite = addSpriteSheet(project, "tower.png", "tower", "static")

    # Add some music
    project.music.append(makeMusic("template", "template.mod"))

    # Set the starting scene
    project.settings["startSceneId"] = project.scenes[0]["id"]
    return project

# Utilities


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Run the generator
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Generate a Game Boy ROM via a GB Studio project file.")
    parser.add_argument('--destination', '-d', type=str,
                        help="destination folder name", default="../gbprojects/projects/")
    parser.add_argument('--assets', '-a', type=str,
                        help="asset folder name", default="assets/")
    args = parser.parse_args()
    initializeGenerator(asset_folder=args.assets)
    project = vijayaGame()
    writeProjectToDisk(project, output_path=args.destination, filename="test.gbsproj")
    if args.destination == "../gbprojects/projects/":
        print(f"{bcolors.WARNING}NOTE: Used default output directory, change with the -d flag{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}See generate.py --help for more options{bcolors.ENDC}")
