import argparse
from rich.console import Console

console = Console()

def first_and_last_number(string: str) -> str:
    nums = [char for char in string if char.isdigit()]
    return f"{nums[0]}{nums[-1]}"

def calibrator(input_file: str) -> list:
    with open(input_file) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        num_strs = [first_and_last_number(string) for string in lines]
        ints = [eval(i) for i in num_strs]
        return ints

def main(input_file: str, verbose: bool):
    parsed_ints = calibrator(input_file)
    if verbose:
        console.print(parsed_ints)
    console.print(f"Sum: {sum(parsed_ints)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.description = "Advent of Code - Day 1: Trebuchet"
    parser.add_argument("-i", "--input_file", help="input file")
    parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true")
    args = parser.parse_args()
    main(args.input_file, args.verbose)
