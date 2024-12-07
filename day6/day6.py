from copy import deepcopy
from time import sleep
import time


def main():
    map_data = load()
    
    part1Answer = part1(map_data)
    print("Part 1: " + str(part1Answer))
    
    start_time = time.time()
    part2Answer = part2(map_data)
    end_time = time.time()
    print(f"Part 2 took {end_time - start_time:.2f} seconds")
    print("Part 2: " + str(part2Answer))
     
def load():
    with open("day6/input.txt") as f:
        lines = f.readlines()
        
    return [list(line.strip()) for line in lines]

def part1(map_data):
    map_data = findRoutePart1(map_data)
    return countVisits(map_data)
            
def findRoutePart1(map_data):
    map_data = deepcopy(map_data)
    
    
    for index, line in enumerate(map_data):
        if '^' in line:
            curr_y = index
            curr_x = line.index('^')
    
    map_data[curr_y][curr_x] = 'X'
    direction = "up"
    
    while True:
        if direction == "up":
            if curr_y <= 0:
                return map_data
            elif map_data[curr_y - 1][curr_x] == '#':
                direction = "right"
            else:
                curr_y -= 1
                map_data[curr_y][curr_x] = 'X'
        elif direction == "right":
            if curr_x >= len(map_data[0]) - 1:
                return map_data
            elif map_data[curr_y][curr_x + 1] == '#':
                direction = "down"
            else:
                curr_x += 1
                map_data[curr_y][curr_x] = 'X'
        elif direction == "down":
            if curr_y >= len(map_data) - 1:
                return map_data
            elif map_data[curr_y + 1][curr_x] == '#':
                direction = "left"
            else:
                curr_y += 1
                map_data[curr_y][curr_x] = 'X'
        elif direction == "left":
            if curr_x <= 0:
                return map_data
            elif map_data[curr_y][curr_x - 1] == '#':
                direction = "up"
            else:
                curr_x -= 1
                map_data[curr_y][curr_x] = 'X'

def countVisits(map_data):
    count = 0
    
    for line in map_data:
        count += line.count('X')
        
    return count


def part2(map_data):
    initialRoute = findRoutePart1(map_data)
    
    count = 0
    
    y = 0
    while y < len(initialRoute):
        x = 0
        while x < len(initialRoute[y]):
            if initialRoute[y][x] == 'X' and map_data[y][x] != '^':
                map_data[y][x] = '#'
                count += (1 if detectLoops(map_data) else 0)
                map_data[y][x] = '.'
            x += 1
        y += 1
        
    return count
    


def detectLoops(map_data):
    map_data = deepcopy(map_data)
    
    map_data = [ [ ( [] if point == '.'  else point )  for point in line ] for line in map_data]
    
    for index, line in enumerate(map_data):
        if '^' in line:
            curr_y = index
            curr_x = line.index('^')
    
    direction = "UP"
    map_data[curr_y][curr_x] = [direction]
    
    while True:
        if direction == "UP":
            if curr_y <= 0:
                return False
            elif map_data[curr_y - 1][curr_x] == '#':
                direction = "RIGHT"
            else:
                curr_y -= 1
                
                if 'UP' in map_data[curr_y][curr_x]:
                    return True  
                map_data[curr_y][curr_x].append('UP')
        elif direction == "RIGHT":
            if curr_x >= len(map_data[0]) - 1:
                return False
            elif map_data[curr_y][curr_x + 1] == '#':
                direction = "DOWN"
            else:
                curr_x += 1
                
                if 'RIGHT' in map_data[curr_y][curr_x]:
                    return True
                map_data[curr_y][curr_x].append('RIGHT')
        elif direction == "DOWN":
            if curr_y >= len(map_data) - 1:
                return False
            elif map_data[curr_y + 1][curr_x] == '#':
                direction = "LEFT"
            else:
                curr_y += 1
                
                if 'DOWN' in map_data[curr_y][curr_x]:
                    return True
                map_data[curr_y][curr_x].append('DOWN')
        elif direction == "LEFT":
            if curr_x <= 0:
                return False
            elif map_data[curr_y][curr_x - 1] == '#':
                direction = "UP"
            else:
                curr_x -= 1

                if 'LEFT' in map_data[curr_y][curr_x]:
                    return True
                map_data[curr_y][curr_x].append('LEFT')
    
if __name__ == "__main__":
    main()
    