from copy import deepcopy

def main():
    grid, actions = load()
    
    part1Answer = solve(grid, actions)
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
                line = line.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
                grid.append(list(line))
        else:
            actions += line
            
    return grid, actions

def solve(grid, actions):
    
    
    robotX, robotY = findRobot(grid)
    
    for idx, action in enumerate(actions):
        print(f"Action: {idx}")
        grid, robotX, robotY = moveRobot(grid, robotX, robotY, action)
        
    
    for line in grid:
        print(''.join(line))
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
    
    newGrid = deepcopy(grid)
    
    success = tryMove(newGrid, moveX, moveY, action)
    
    
    if success:
        newGrid[moveY][moveX], newGrid[y][x] = newGrid[y][x], newGrid[moveY][moveX]
        return newGrid, moveX, moveY
    else:
        return grid, x, y
    

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

def verticalMove(action):
    return action in ["^", "v"]

def tryMove(grid, x, y, action, side = False):
    if grid[y][x] == "#":
        return False
    elif grid[y][x] in ['[' , ']']:
        moveX, moveY = movementCoords(x, y, action)
        
        if verticalMove(action):

            moveStorageResult = True 
            if not side:   
                if grid[y][x] == "[":
                    moveStorageResult = tryMove(grid, x + 1, y, action, side=True)
                else:
                    moveStorageResult = tryMove(grid, x - 1, y, action, side=True)
                
            moveStorageResult = tryMove(grid, moveX, moveY, action) and moveStorageResult

        else:
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
            if grid[y][x] == "[":
                gpsCoordinates.append(x + 100*y)
    return gpsCoordinates

if __name__ == "__main__":
    main()