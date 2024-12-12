def main():
    mapData = load()
    
    part1Answer = part1(mapData)
    print(f"Part 1: {part1Answer}")
    
    part2Answer = part2(mapData)
    print(f"Part 2: {part2Answer}")
    

def load():
    with open('day10/input.txt', 'r') as f:
        lines = f.readlines()
        return [[ -1 if char == '.' else int(char) for char in line.strip()] for line in lines]

def part1(mapData):
    
    scores = []
    
    startY = 0
    
    while startY < len(mapData):
        startX = 0
        while startX < len(mapData[startY]):
            if mapData[startY][startX] == 0:
                scores.append(len(findScorePart1(mapData, startY, startX)))
            
            startX += 1
        startY += 1    
        
    return sum(scores)
        
        
def findScorePart1(mapData, y, x):
    currValue = mapData[y][x]
    
    if currValue == 9:
        return [f"{x}, {y}"]
    
    topMountains = []
    
    if checkValid(mapData, currValue, y - 1, x):
        topMountains.extend(findScorePart1(mapData, y - 1, x))
    
    if checkValid(mapData, currValue, y + 1, x):
        topMountains.extend(findScorePart1(mapData, y + 1, x))
        
    if checkValid(mapData, currValue, y, x - 1):
        topMountains.extend(findScorePart1(mapData, y, x - 1))
        
    if checkValid(mapData, currValue, y, x + 1):
        topMountains.extend(findScorePart1(mapData, y, x + 1))
        
    return list(dict.fromkeys(topMountains))
    
def part2(mapData):
    
    scores = []
    
    startY = 0
    
    while startY < len(mapData):
        startX = 0
        while startX < len(mapData[startY]):
            if mapData[startY][startX] == 0:
                scores.append(len(findScorePart2(mapData, startY, startX)))
            
            startX += 1
        startY += 1    
        
    return sum(scores)
        
        
def findScorePart2(mapData, y, x):
    currValue = mapData[y][x]
    
    if currValue == 9:
        return [f"{x}, {y}"]
    
    topMountains = []
    
    if checkValid(mapData, currValue, y - 1, x):
        topMountains.extend(findScorePart2(mapData, y - 1, x))
    
    if checkValid(mapData, currValue, y + 1, x):
        topMountains.extend(findScorePart2(mapData, y + 1, x))
        
    if checkValid(mapData, currValue, y, x - 1):
        topMountains.extend(findScorePart2(mapData, y, x - 1))
        
    if checkValid(mapData, currValue, y, x + 1):
        topMountains.extend(findScorePart2(mapData, y, x + 1))
        
    return topMountains
    


def checkValid(mapData, currentValue , y, x):
    if y < 0 or y >= len(mapData):
        return False
    
    if x < 0 or x >= len(mapData[y]):
        return False
    
    return mapData[y][x] == currentValue + 1


    
    

if __name__ == '__main__':
    main()