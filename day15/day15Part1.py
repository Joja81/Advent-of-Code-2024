from copy import deepcopy

def main():
    grid, actions = load()
    
    part1Answer = part1(grid, actions)
    print(f"Part 1 Answer {part1Answer}")

def load():
    with open("day15/input.txt") as f:
        lines = f.readlines()
        
    lines = [line.strip() for line in lines]

    grid = []
    actions = ""
    
    loadingGrid = True
    for line in lines:
        if loadingGrid:
            if line == "":
                loadingGrid = False
            else:
                grid.append(list(line))
        else:
            actions += line
            
    return grid, actions

def part1(grid, actions):
    
    robotX, robotY = findRobot(grid)
    
    for action in actions:
        robotX, robotY = moveRobot(grid, robotX, robotY, action)
        
    gpsCoordinates = findGPS(grid)
    return sum(gpsCoordinates)
    
    
def findRobot(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                return x, y
    raise Exception("No robot found")
    
def moveRobot(grid, x, y, action):
    moveX, moveY = movementCoords(x, y, action)
    
    success = tryMove(grid, moveX, moveY, action)
    
    
    if success:
        grid[moveY][moveX], grid[y][x] = grid[y][x], grid[moveY][moveX]
        return moveX, moveY
    else:
        return x, y
    

def movementCoords(x, y, action):
    if action == "^":
        return x, y - 1
    elif action == "v":
        return x, y + 1
    elif action == ">":
        return x + 1, y
    elif action == "<":
        return x - 1, y
    else:
        raise Exception("Invalid action")


def tryMove(grid, x, y, action):
    if grid[y][x] == "#":
        return False
    elif grid[y][x] == "O":
        moveX, moveY = movementCoords(x, y, action)
        moveStorageResult = tryMove(grid, moveX, moveY, action)
        if moveStorageResult:
            grid[moveY][moveX], grid[y][x] = grid[y][x], grid[moveY][moveX]
            return True
        else:
            return False
    else:
        return True
        
    
def findGPS(grid):
    gpsCoordinates = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "O":
                gpsCoordinates.append(x + 100*y)
    return gpsCoordinates

if __name__ == "__main__":
    main()