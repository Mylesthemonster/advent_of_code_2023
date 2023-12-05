import argparse
from rich.console import Console

console = Console()

def cube_validator(string: str, verbose: bool) -> int:
    match = string.split(";")
    match[0] = match[0].split(":")[1]
    games_played = [x.replace("," , "") for x in match]
    games_played = [x.strip() for x in games_played]
    if verbose:
        console.print(games_played)
        
    MAX_RED=12 
    MAX_GREEN=13
    MAX_BLUE=14
    valid_game = 1
    
    for games in games_played:
        single_game = games.split()
        for i in range(0, len(single_game), 2):
            cubes = int(single_game[i])
            color = single_game[i+1]
            if color == 'red' and cubes > MAX_RED:
                if verbose:
                    console.print(f'Too many {color} cubes')
                valid_game = 0
                break
            elif color == 'green' and cubes > MAX_GREEN:
                if verbose:
                    console.print(f'Too many {color} cubes')
                valid_game = 0
                break
            elif color == 'blue' and cubes > MAX_BLUE:
                if verbose:
                    console.print(f'Too many {color} cubes')
                valid_game = 0
                break

    return valid_game

def game_checker(input_file: str, verbose: bool) -> int:
    with open(input_file) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        valid_games = [cube_validator(string, verbose) for string in lines]
        if verbose:
            console.print(valid_games)
        valid_game_index_sum = 0
        for i, v in enumerate(valid_games):
            if v == 1:
                valid_game_index_sum += i + 1
        return valid_game_index_sum

def main(input_file: str, verbose: bool):
    valid_game_index_sum = game_checker(input_file, verbose)
    console.print(f"Sum of game IDs of the games that would have been possible: {valid_game_index_sum}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.description = "Advent of Code - Day 2: Cube Conundrum"
    parser.add_argument("-i", "--input_file", help="input file")
    parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true")
    args = parser.parse_args()
    main(args.input_file, args.verbose)
