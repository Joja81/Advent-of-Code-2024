
from queue import PriorityQueue


# X_SIZE = 7
# Y_SIZE = 7

# SIMULATE_LENGTH = 12

X_SIZE = 71
Y_SIZE = 71

SIMULATE_LENGTH = 1024

def main():
    dropCoordinates = load()
    
    part1Answer = part1(dropCoordinates[:SIMULATE_LENGTH])
    print(f"Part 1 Answer: {part1Answer}")
    
    part2Answer = part2(dropCoordinates)
    print(f"Part 2 Answer: {part2Answer}")
    
def load():
    with open("day18/input.txt") as f:
        lines = f.readlines()
        
    return [ ( int(line.split(',')[0].strip()), int(line.split(',')[1].strip())  ) for line in lines ]
    
def part1(dropCoordinates):
    grid = loadGrid(dropCoordinates)
    distances = [[None for _ in range(X_SIZE)] for _ in range(Y_SIZE)]
    
    queue = PriorityQueue()
    
    queue.put((0, 0, 0))
    
    while not queue.empty():
        distance, x, y = queue.get()
        
        explore(distance, x, y, grid, distances, queue)
        
    return distances[-1][-1]
    
def part2(dropCoordinates):
    
    bytesDropped = SIMULATE_LENGTH
    
    while( part1(dropCoordinates[:bytesDropped]) != None):
        bytesDropped += 1
        print(bytesDropped)
    
    return dropCoordinates[bytesDropped - 1]
    

def explore(distance, x, y, grid, distances, queue: PriorityQueue):
    if distances[y][x] != None and distances[y][x] <= distance:
        return
    
    distances[y][x] = distance
    
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    
    for xMove, yMove in moves:
        
        newX = x + xMove
        newY = y + yMove
        
        if newX < 0 or newX >= len(grid[y]):
            continue
        elif newY < 0 or newY >= len(grid):
            continue
        elif grid[newY][newX]:
            continue
        
        queue.put((distance + 1, newX, newY))
         
    
    
        
        
        
def loadGrid(dropCoordinates):
    grid = [[False for _ in range(X_SIZE)] for _ in range(Y_SIZE)]
    
    for x, y in dropCoordinates:
        grid[y][x] = True
        
    return grid


if __name__ == "__main__":
    main()