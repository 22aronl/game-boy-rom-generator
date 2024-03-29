import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir,"rom_generator"))

import generator
import level_generator

def test_RockWorld(tmpdir):
    generator.initializeGenerator(asset_folder = "assets/")
    project = level_generator.createRockWorld()
    generator.writeProjectToDisk(project, output_path = tmpdir)
    assert(project.scenes[0]["x"] == 200)
    assert(project.scenes[0]["actors"][0]["movementType"] == "static")
    assert(project.scenes[0]["triggers"][0]["script"][1]["command"] == "EVENT_END")
    assert(project.spriteSheets[1]["name"] == "rock")
    assert(project.backgrounds[0]["name"] == "placeholder")
    assert(project.backgrounds[0]["height"] == 18)
