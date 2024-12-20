import re
from functools import reduce
from operator import mul

# X_SIZE = 11
# Y_SIZE = 7

X_SIZE = 101
Y_SIZE = 103
TIME = 100


def main():
    robots = load()
    
    # part1Answer = part1(robots)
    # print(f"Part 1 Answer {part1Answer}")
    
    part2(robots)
    
    
def load():
    with open("day14/input.txt") as f:
        lines = f.readlines()
        
    return [parseRobot(line) for line in lines]
    
def parseRobot(line):
    results = re.search(r'p=([\d]+,[\d]+)[ ]v=(-?[\d]+,-?[\d]+)', line)
    
    return {
        'position': tuple(map(int, results.group(1).split(','))),
        'velocity': tuple(map(int, results.group(2).split(',')))
    }
 
def part1(robots):
    for _ in range(TIME):
        for robot in robots:
            moveRobot(robot)
            
    grid = robotGrid(robots)
    
        
    quadrants = scoreQuadrants(grid)
    return reduce(mul, quadrants)

def moveRobot(robot):
    robot['position'] = (robot['position'][0] + robot['velocity'][0], robot['position'][1] + robot['velocity'][1])
    
    if robot['position'][0] < 0:
        robot['position'] = (X_SIZE +  robot['position'][0], robot['position'][1])
    elif robot['position'][0] >= X_SIZE:
        robot['position'] = (robot['position'][0] - X_SIZE, robot['position'][1])
        
    if robot['position'][1] < 0:
        robot['position'] = (robot['position'][0], Y_SIZE + robot['position'][1])
    elif robot['position'][1] >= Y_SIZE:
        robot['position'] = (robot['position'][0], robot['position'][1] - Y_SIZE    )

def robotGrid(robots):
    grid = [[0 for _ in range(X_SIZE)] for _ in range(Y_SIZE)]
    
    for robot in robots:
        grid[robot['position'][1]][robot['position'][0]] += 1
        
    return grid

def scoreQuadrants(grid):
    quadrants = []
    
    yHalf = Y_SIZE // 2
    xHalf = X_SIZE // 2
    
    # top left
    quadrants.append(
        sum([grid[y][x] for y in range(yHalf) for x in range(xHalf)])
    )
    # top right
    quadrants.append(
        sum([grid[y][x] for y in range(yHalf) for x in range(xHalf + 1, X_SIZE)])
    )
    # bottom left
    quadrants.append(
        sum([grid[y][x] for y in range(yHalf + 1, Y_SIZE) for x in range(xHalf)])
    )
    # bottom right
    quadrants.append(
        sum([grid[y][x] for y in range(yHalf + 1, Y_SIZE) for x in range(xHalf + 1, X_SIZE)])
    )
    
    return quadrants
    
def part2(robots):
    run = 0
    while True:
        run += 1
        if run % 1000 == 0:
            print(f"Run {run}")
        
        for robot in robots:
            moveRobot(robot)
            
        grid = robotGrid(robots)
        
        for row in grid:
            if any(row[i:i+30].count(0) == 0 for i in range(len(row) - 49)):
                for row in grid:
                    print(''.join(['#' if x > 0 else '.' for x in row]))
                    
                print(f'\n\n{run}',)
                return
    
    
    

if __name__ == "__main__":
    main()