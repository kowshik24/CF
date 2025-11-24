import sys

def main():
    # Read input from stdin
    input_line = sys.stdin.readline().strip()
    
    # Parse the integer after "Game "
    try:
        round_number = int(input_line.split()[1])
    except (IndexError, ValueError):
        return  # Exit if parsing fails
    
    # Always drop the chip in column 8 (center of 17 columns: 0..16)
    print(8)

if __name__ == "__main__":
    main()
