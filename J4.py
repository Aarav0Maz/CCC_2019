def flipper(operations):
    grid = [[1, 2], [3, 4]]

    for op in operations:
        if op == 'H':
            # Horizontal flip
            grid = [grid[1], grid[0]]
        elif op == 'V':
            # Vertical flip
            new_grid = []
            for row in grid:
                new_grid.append(row[::-1])
            grid = new_grid

    return grid

def main():
    # Input
    operations = input().strip()

    # Process the operations
    final_grid = flipper(operations)

    # Output
    for row in final_grid:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()  
