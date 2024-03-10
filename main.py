from src.components import show_app_title

from src.config import load_instance_config

from src.arduino import get_arduino_instance

from src.http import get_team_last_game


if __name__ == "__main__":

    load_instance_config()

    red = 11
    green = 6
    blue = 5

    pins = [red, green, blue]

    board = get_arduino_instance('COM5', pins)

    show_app_title()

    last_game = get_team_last_game("kings")

    season_id = last_game["SEASON_ID"]

    if last_game["WL"] == "W":
        print(season_id)
        print("LIGHT THE BEAM")


        board.digital[red].write(1)
        board.digital[blue].write(1)
        board.digital[green].write(0)