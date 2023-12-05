import argparse
from rich.console import Console

console = Console()

SYMBOLS=['*', '-', '%', '$', '=', '@', '#', '/', '&', '+']

def sum_part_numbers(input_file: str, verbose: bool) -> int:
    part_numbers = {}
    with open(input_file) as f:
        lines = f.readlines()
        schematic = [line.strip() for line in lines]
        rows = len(schematic)
        columns = len(schematic[0])

        for i in range(rows):
            for j in range(columns):
                char = schematic[i][j]
                if char in SYMBOLS:
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue
                            
                            x = i + dx
                            y = j + dy
                            
                            if 0 <= x < rows and 0 <= y < columns:
                                adj = schematic[x][y]
                                if adj.isdigit():
                                    digits = []
                                    digits.append(adj)

                                    left = y - 1
                                    right = y + 1
                                    
                                    while left >= 0 and schematic[x][left] != ".":
                                        if schematic[x][left] in SYMBOLS: # check if left character is a symbol
                                            break # break the loop if it is
                                        digits.insert(0, schematic[x][left])
                                        left -= 1

                                    while right < columns and schematic[x][right] != ".":
                                        if schematic[x][right] in SYMBOLS: # check if right character is a symbol
                                            break # break the loop if it is
                                        digits.append(schematic[x][right])
                                        right += 1
                                        
                                    # if digits[-1] in SYMBOLS:
                                    #     digits.pop()
                                    
                                    # if digits[0] in SYMBOLS:
                                    #     digits.pop(0)

                                    num_str = "".join(digits) 
                                    # for symbol in SYMBOLS: 
                                    #     num_str = num_str.replace(symbol, "")
                                    num = int(num_str)
                                    
                                    if (x, y) in part_numbers:
                                        pos = part_numbers[(x, y)]
                                        if abs(pos - i) <= 1 and abs(pos - j) <= 1:
                                            pass
                                        else:
                                            part_numbers[(x, y)] = (num)
                                    else:
                                        part_numbers[(x, y)] = (num)
        
        if verbose:
            console.print(part_numbers.values())
        dupes = set() 
        for k, v in list(part_numbers.items()):
            if v in dupes: 
                del part_numbers[k]
            else:
                dupes.add(v)
        if verbose:
            console.print(part_numbers.values())
    return sum(part_numbers.values())

def main(input_file: str, verbose: bool):
    part_num_sum = sum_part_numbers(input_file, verbose)
    console.print(f"Sum of all of the part numbers in the engine schematic = {part_num_sum}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.description = "Advent of Code - Day 3: Gear Ratios"
    parser.add_argument("-i", "--input_file", help="input file")
    parser.add_argument("-v", "--verbose", help="Verbose output", action="store_true")
    args = parser.parse_args()
    main(args.input_file, args.verbose)