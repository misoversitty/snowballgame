from pathlib import Path


GAME_DIRECTORY = Path("D:\my shit\ProgProjects\snowballgame\Project")
GAME_DIRECTORY = Path.cwd()
RESOURCES_DIRECTORY = Path.joinpath(GAME_DIRECTORY, "Resources")
SETTINGS_DIRECTORY = Path.joinpath(GAME_DIRECTORY, "Settings")

NUMBER_OF_PLAYERS = 1
